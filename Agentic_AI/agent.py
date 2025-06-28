from google.genai import types
from Agentic_AI.base_agent import TracerAgent


code_path = r"Agentic_AI\LLM_Files\test_case1.txt"
with open(code_path, "r") as file:
    input_code = file.read()

prompt_path = r"Agentic_AI\LLM_Files\system_prompt.txt"
with open(prompt_path, "r") as file:
    prompt = file.read()


#This function declares the drawing functions in the OpenAPI Schema, which is what Gemini requires for it's configuration
def declare_drawing_functions():
    functions = [
        {
            "name": "draw_node",
            "description": "Custom pygame drawing function. Draws a node with text value inside, the node can be resized by passing in coordinates and there is a boolean parameter to highlight the node.",
            "parameters": 
            {
                "type": "object",
                "properties": 
                {
                    "value": 
                    {
                        "type": "number",
                        "description": "The value that will go within the node"
                    },
                    
                    "coordinates": 
                    {
                        "type": "array",
                        "description": "The (x,y) coordinates for where you want to draw the node within the screen",
                        "items": {"type": "number"},
                        "minItems": 2,
                        "maxItems": 2,
                    },
                        
                    "rectangle_width": 
                    {
                        "type": "integer",
                        "description": "The width of the rectangle. The minimum width is 40",
                        "minimum": 50,
                        "maximum": 150,
                    },
                    
                    "rectangle_height": 
                        {
                        "type": "integer",
                        "description": "The height of the rectangle.",
                        "minimum": 50,
                        "maximum": 150
                    },
                        
                    "highlight": 
                    {
                        "type": "boolean",
                        "description": "To highlight the node, set to true"
                    },
                    
                    "error": 
                    {
                        "type": "boolean",
                        "description": "For a node with errors, set to true and we will highlight it red"
                    },
                    
                    "animation_frame": 
                    {
                        "type": "number",
                        "description": "You can group drawings into frames! Sequentially group your drawings together to visualize each line of code. You must use all 20 animation frames.",
                        "minimum":0,
                        "maximum": 20,
                    },
                },
                "required": ["value", "coordinates", "rectangle_width", "rectangle_height", "error", "highlight", "animation_frame"]
            }
        },

        {
            "name": "draw_text",
            "description": "Custom pygame drawing function. Draws a text anywhere on the screen",
            "parameters": 
            {
                "type": "object",
                "properties": 
                {
                    "text": 
                    {
                        "type": "string",
                        "description": "Only variable names are allowed",
                        "maxLength": 5,
                    },
                    
                    "coordinates": 
                    {
                        "type": "array",
                        "description": "The (x,y) coordinates for where you want to draw the node within the screen",
                        "items": {"type": "number"},
                        "minItems": 2,
                        "maxItems": 2
                    },
                    
                    "font_size": 
                    {
                        "type": "number",
                        "description": "The size of the font in pixels for the text you are drawing",
                        "minimum": 30,
                        "maximum": 50,
                    },
                    
                    "animation_frame": 
                    {
                        "type": "number",
                        "description": "You can group drawings into frames! Sequentially group your drawings together to visualize each line of code, You must use all 20 animation frames.",
                        "minimum":0,
                        "maximum": 20,
                    },
                },
                "required": ["text", "coordinates", "font_size", "animation_frame"]
            }
        },

        {
            "name": "draw_arrow",
            "description": "Custom pygame drawing function. Draws an arrow anywhere on the screen",
            "parameters": 
            {
                "type": "object",
                "properties": 
                {
                    "start_pos": 
                    {
                        "type": "array",
                        "description": "The (x,y) coordinate for the starting point of the arrow",
                        "items": {"type": "number"},
                        "minItems": 2,
                        "maxItems": 2
                    },
                    
                    "end_pos": 
                    {
                        "type": "array",
                        "description": "The (x,y) coordinates for the ending point of the arrow, the arrow's tip",
                        "items": {"type": "number"},
                        "minItems": 2,
                        "maxItems": 2
                    },
                    
                    "animation_frame": 
                    {
                        "type": "number",
                        "description": "You can group drawings into frames! Sequentially group your drawings together to visualize each line of code. You must use all 20 animation frames.",
                        "minimum":0,
                        "maximum": 20,
                    },
                },
                "required": ["start_pos", "end_pos", "animation_frame"]
            }
        }
    ]
    return functions


def gemini_tracer(api_key):
    drawing_tools = [types.Tool(function_declarations=declare_drawing_functions())]

    #Configure Gemini to our specifications!
    config = types.GenerateContentConfig(
        system_instruction=prompt,
        temperature=1.5,
        tools=drawing_tools,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False), #These are helpful according to the documentation
        tool_config=types.ToolConfig(function_calling_config=types.FunctionCallingConfig(mode='ANY')),
    )

    #Passing in the input
    contents = types.Content(role="user", parts=[types.Part(text=input_code)])

    #Instantiate the agent
    agent = TracerAgent(api_key)

    #Load the agent and call trace from base_agent.py
    Decided_Functions = agent.trace(contents, config)
    
    #Returns a list of function calls with their names and their arguments
    return Decided_Functions.function_calls

if __name__ == '__main__':
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_key = os.getenv("GEMINI_KEY")

    print(gemini_tracer(api_key))
