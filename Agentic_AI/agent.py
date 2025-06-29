from google.genai import types
from Agentic_AI.base_agent import TracerAgent


code_path = r"Agentic_AI\LLM_Files\test_case1.txt"
code_path_linux = r"Agentic_AI/LLM_Files/test_case1.txt"
try:
    with open(code_path, "r") as file:
        input_code = file.read()
except:
    with open(code_path_linux, "r") as file:
        input_code = file.read()

prompt_path = r"Agentic_AI\LLM_Files\system_prompt.txt"
prompt_path_linux = r"Agentic_AI/LLM_Files/system_prompt.txt"
try:
    with open(prompt_path, "r") as file:
        prompt = file.read()
except:
    with open(prompt_path_linux, "r") as file:
        prompt = file.read()

max_frames = 30


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
                        "minimum": 100,
                        "maximum": 200,
                    },
                    
                    "rectangle_height": 
                        {
                        "type": "integer",
                        "description": "The height of the rectangle.",
                        "minimum": 100,
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
                        "description": "You can group drawings into frames! Sequentially group your drawings together to visualize each line of code. You must use all {max_frames} animation frames.",
                        "minimum":0,
                        "maximum": max_frames,
                    },
                },
                "required": ["value", "coordinates", "rectangle_width", "rectangle_height", "error", "highlight", "animation_frame"]
            }
        },

        {
            "name": "draw_text",
            "description": "Draw explanations for why you drew certain visualizations to explain code.",
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
                        "maximum": 30,
                    },
                    
                    "animation_frame": 
                    {
                        "type": "number",
                        "description": f"You can group drawings into frames! Sequentially group your drawings together to visualize each line of code, You must use all {max_frames} animation frames.",
                        "minimum":0,
                        "maximum": max_frames,
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
                        "description": f"You can group drawings into frames! Sequentially group your drawings together to visualize each line of code. You must use all {max_frames} animation frames.",
                        "minimum":0,
                        "maximum": max_frames,
                    },
                },
                "required": ["start_pos", "end_pos", "animation_frame"]
            }
        },

        {
            "name": "draw_circular_node",
            "description": "Custom pygame drawing function. Draws a circular node for describing computer science data structures.",
            "parameters": 
            {
                "type": "object",
                "properties": 
                {
                    "value": 
                    {
                        "type": "number",
                        "description": "The value stored within this node.",
                    },
                    
                    "center": 
                    {
                        "type": "array",
                        "description": "The (x,y) center coordinate for this circle",
                        "items": {"type": "number"},
                        "minItems": 2,
                        "maxItems": 2
                    },

                    "radius": 
                    {
                        "type": "number",
                        "description": "The radius of the circular node.",
                        "minimum":50,
                        "maximum":150
                    },

                    "animation_frame": 
                    {
                        "type": "number",
                        "description": "You can group drawings into frames! Sequentially group your drawings together to visualize each line of code. You must use all {max_frames} animation frames.",
                        "minimum":0,
                        "maximum": max_frames,
                    },
                },
                "required": ["value", "center", "radius", "animation_frame"]
            }
        }
    ]
    return functions


def gemini_tracer(api_key, input_code, backup_input=""):
    drawing_tools = [types.Tool(function_declarations=declare_drawing_functions())]

    sys_prompt = prompt + str(backup_input)
    #Configure Gemini to our specifications!
    config = types.GenerateContentConfig(
        system_instruction=sys_prompt,
        temperature=1.8,
        tools=drawing_tools,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False), #These are helpful according to the documentation
        tool_config=types.ToolConfig(function_calling_config=types.FunctionCallingConfig(mode='ANY')),
    )

    text = str(input_code) + str(backup_input)
    
    #Passing in the input
    contents = types.Content(role="user", parts=[types.Part(text=text)])

    #Instantiate the agent
    agent = TracerAgent(api_key)

    #Load the agent and call trace from base_agent.py
    Decided_Functions = agent.trace(contents, config, model="gemini-2.0-flash-lite")
    
    #Returns a list of function calls with their names and their arguments
    return Decided_Functions.function_calls



def double_check(api_key, input_code, function_calls: str):
    BackUp = TracerAgent(api_key)

    #Configure Gemini to our specifications!
    config = types.GenerateContentConfig(
        system_instruction="You are programming tutor who is supposed to help an AI Agent make proper function calls to visualize students' code. The agent should use draw_text very sparringly and should draw many of the other shapes to creatively visualize code. you will be given input code and the AI Agent's recommended function and your goal is to write a detailed system prompt file in order to guide the AI Agent to make the best possible visualizations. The AI Agent already knows how to call the functions, so write your response in plain english",
        temperature=1.7
    )

    contents = types.Content(role="user", parts=[types.Part(text=function_calls)])

    response = BackUp.trace(contents, config, model="gemini-2.0-flash-lite")
    file_path = "Agentic_AI\LLM_Files\logic_tweaks.txt"


    with open(file_path, "w") as file:
        file.write(response.text)
    
    function_list = gemini_tracer(api_key, input_code, backup_input=response)
    return function_list


    
    
if __name__ == '__main__':
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_key = os.getenv("GEMINI_KEY")

    print(gemini_tracer(api_key))
