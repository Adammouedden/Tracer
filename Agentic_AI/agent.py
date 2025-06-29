from google.genai import types
from Agentic_AI.base_agent import TracerAgent


code_path = r"Agentic_AI\LLM_Files\bst_testcase.txt"
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
            "description": "This function draws a rectangular node, representing a data structure element, with an optional value inside. You can customize the size, highlight the node for emphasis, and flag it with an error state (colored red). The node’s position on the screen is controlled by its coordinates, and you can animate the node's appearance within a given frame for sequential code visualization.",
            "parameters": 
            {
                "type": "object",
                "properties": 
                {
                    "value": 
                    {
                        "type": "number",
                        "description": "The value to be displayed within the node, representing the data or element in the structure."
                    },
                    
                    "coordinates": 
                    {
                        "type": "array",
                        "description": "The (x, y) coordinates for the node's placement on the screen.",
                        "items": {"type": "number"},
                        "minItems": 2,
                        "maxItems": 2,
                    },
                        
                    "rectangle_width": 
                    {
                        "type": "integer",
                        "description": "The width of the node’s rectangle. The minimum allowed width is 40 pixels.",
                        "minimum": 100,
                        "maximum": 200,
                    },
                    
                    "rectangle_height": 
                        {
                        "type": "integer",
                        "description": "The height of the node’s rectangle.",
                        "minimum": 100,
                        "maximum": 150
                    },
                        
                    "highlight": 
                    {
                        "type": "boolean",
                        "description": "Set to true to highlight the node visually for emphasis (useful for indicating important or active nodes)."
                    },
                    
                    "error": 
                    {
                        "type": "boolean",
                        "description": "If true, the node will be colored red, indicating it contains an error or special case to be addressed."
                    },
                    
                    "animation_frame": 
                    {
                        "type": "number",
                        "description": "Indicates which frame the drawing belongs to. Group your drawings across frames to visualize the sequential steps of code execution. Ensure all {max_frames} frames are used to maintain continuity.",
                        "minimum": 0,
                        "maximum": max_frames,
                    },
                },
                "required": ["value", "coordinates", "rectangle_width", "rectangle_height", "error", "highlight", "animation_frame"]
            }
        },

        {
            "name": "draw_text",
            "description": "This function draws a text label that explains the visualization. It is typically used to display variable names or annotations that clarify the purpose of the visualized nodes or data structures. The position and size of the text can be customized, and it can be grouped into animation frames for sequential code explanation.",
            "parameters": 
            {
                "type": "object",
                "properties": 
                {
                    "text": 
                    {
                        "type": "string",
                        "description": "A brief explanation or variable name to display. Only variable names (up to 5 characters) are allowed for clarity."
                    },
                    
                    "coordinates": 
                    {
                        "type": "array",
                        "description": "The (x, y) coordinates where the text should be placed on the screen, typically near the associated nodes or structures.",
                        "items": {"type": "number"},
                        "minItems": 2,
                        "maxItems": 2
                    },
                    
                    "font_size": 
                    {
                        "type": "number",
                        "description": "The size of the font in pixels, fixed at 30 pixels to ensure clarity."
                    },
                    
                    "animation_frame": 
                    {
                        "type": "number",
                        "description": "Indicates which frame the text belongs to, used for synchronizing annotations with visualizations. All frames must be used sequentially to maintain accurate flow.",
                        "minimum": 0,
                        "maximum": max_frames,
                    },
                },
                "required": ["text", "coordinates", "font_size", "animation_frame"]
            }
        },

        {
            "name": "draw_arrow",
            "description": "This function draws an arrow between two points on the screen to illustrate relationships, such as the flow of execution or connections between data structure elements. The start and end coordinates are defined, and the drawing can be animated to show the progression of data or logic over time.",
            "parameters": 
            {
                "type": "object",
                "properties": 
                {
                    "start_pos": 
                    {
                        "type": "array",
                        "description": "The (x, y) coordinates for the starting point of the arrow. Typically used to show the origin of a pointer or data flow.",
                        "items": {"type": "number"},
                        "minItems": 2,
                        "maxItems": 2                    
                    },
                    
                    "end_pos": 
                    {
                        "type": "array",
                        "description": "The (x, y) coordinates where the text should be placed on the screen, typically near the associated nodes or structures.",
                        "items": {"type": "number"},
                        "minItems": 2,
                        "maxItems": 2
                    },
                    
                    "animation_frame": 
                    {
                        "type": "number",
                        "description": "Indicates which frame the arrow should be drawn in, allowing the visualization to match the execution steps in the code. Make sure to include all {max_frames} frames for complete visualization.",
                        "minimum": 0,
                        "maximum": max_frames,
                    },
                },
                "required": ["start_pos", "end_pos", "animation_frame"]
            }
        },
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

    input = str(function_calls) + str(input_code)
    contents = types.Content(role="user", parts=[types.Part(text=input)])

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
