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
            "description": "Draw a rectangular **node** for a data structure element. Include its `value`. Use `highlight=true` for active/traversed nodes and `error=true` for erroneous states. Position with `coordinates`. Crucially, set `animation_frame` to show its state in the sequence of execution.",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "number",
                        "description": "The value to be displayed within the node, representing the data or element in the structure."
                    },
                    "coordinates": {
                        "type": "array",
                        "description": "The (x, y) coordinates for the node's placement on the screen.",
                        "items": {
                            "type": "number"
                        },
                        "minItems": 2,
                        "maxItems": 2
                    },
                    "rectangle_width": {
                        "type": "integer",
                        "description": "The width of the node’s rectangle. The minimum allowed width is 40 pixels.",
                        "minimum": 100,
                        "maximum": 200
                    },
                    "rectangle_height": {
                        "type": "integer",
                        "description": "The height of the node’s rectangle.",
                        "minimum": 100,
                        "maximum": 150
                    },
                    "highlight": {
                        "type": "boolean",
                        "description": "Set to true to highlight the node visually for emphasis (useful for indicating important or active nodes)."
                    },
                    "error": {
                        "type": "boolean",
                        "description": "If true, the node will be colored red, indicating it contains an error or special case to be addressed."
                    },
                    "animation_frame": {
                        "type": "number",
                        "description": "Indicates which frame the drawing belongs to. Group your drawings across frames to visualize the sequential steps of code execution. Ensure all {max_frames} frames are used to maintain continuity.",
                        "minimum": 0,
                        "maximum": f"{max_frames}"
                    }
                },
                "required": [
                    "value",
                    "coordinates",
                    "rectangle_width",
                    "rectangle_height",
                    "error",
                    "highlight",
                    "animation_frame"
                ]
            }
        },
        {
            "name": "draw_text",
            "description": "Draw a **text label** (e.g., variable names up to 5 characters, 'head', 'tail', 'root', 'idx') to explain elements or concepts. Position with `coordinates`. Ensure `font_size` is 30. Use `animation_frame` to synchronize with visualization steps.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "A brief explanation or variable name to display. Only variable names (up to 5 characters) are allowed for clarity."
                    },
                    "coordinates": {
                        "type": "array",
                        "description": "The (x, y) coordinates where the text should be placed on the screen, typically near the associated nodes or structures.",
                        "items": {
                            "type": "number"
                        },
                        "minItems": 2,
                        "maxItems": 2
                    },
                    "font_size": {
                        "type": "number",
                        "description": "The size of the font in pixels, fixed at 30 pixels to ensure clarity."
                    },
                    "animation_frame": {
                        "type": "number",
                        "description": "Indicates which frame the text belongs to, used for synchronizing annotations with visualizations. All frames must be used sequentially to maintain accurate flow.",
                        "minimum": 0,
                        "maximum": f"{max_frames}"
                    }
                },
                "required": [
                    "text",
                    "coordinates",
                    "font_size",
                    "animation_frame"
                ]
            }
        },
        {
            "name": "draw_arrow",
            "description": "Draw an **arrow** to indicate pointers, connections (e.g., linked list `next`, tree child pointers), or traversal paths. Define `start_pos` and `end_pos`. Use `animation_frame` to show the dynamic relationships and flow.",
            "parameters": {
                "type": "object",
                "properties": {
                    "start_pos": {
                        "type": "array",
                        "description": "The (x, y) coordinates for the starting point of the arrow. Typically used to show the origin of a pointer or data flow.",
                        "items": {
                            "type": "number"
                        },
                        "minItems": 2,
                        "maxItems": 2
                    },
                    "end_pos": {
                        "type": "array",
                        "description": "The (x, y) coordinates where the text should be placed on the screen, typically near the associated nodes or structures.",
                        "items": {
                            "type": "number"
                        },
                        "minItems": 2,
                        "maxItems": 2
                    },
                    "animation_frame": {
                        "type": "number",
                        "description": "Indicates which frame the arrow should be drawn in, allowing the visualization to match the execution steps in the code. Make sure to include all {max_frames} frames for complete visualization.",
                        "minimum": 0,
                        "maximum": f"{max_frames}"
                    }
                },
                "required": [
                    "start_pos",
                    "end_pos",
                    "animation_frame"
                ]
            }
        },
        {
            "name": "draw_circular_node",
            "description": "This function draws a circular node, often used to represent elements in data structures like trees or graphs where a circular shape is more intuitive than a rectangle. You can specify its value, position (center coordinates), radius, and color. The width parameter controls the thickness of the circle's outline.",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "number",
                        "description": "The numerical value to be displayed inside the circular node."
                    },
                    "center": {
                        "type": "array",
                        "description": "The [x, y] coordinates for the center of the circular node.",
                        "items": {
                            "type": "number"
                        },
                        "minItems": 2,
                        "maxItems": 2
                    },
                    "radius": {
                        "type": "number",
                        "description": "The radius of the circular node in pixels. Must be a positive value.",
                        "minimum": 10
                    },
                    "animation_frame": {
                        "type": "number",
                        "description": "Indicates which frame the drawing belongs to. Group your drawings across frames to visualize the sequential steps of code execution. Ensure all {max_frames} frames are used to maintain continuity.",
                        "minimum": 0,
                        "maximum": f"{max_frames}"
                    }
                },
                "required": [
                    "value",
                    "center",
                    "radius",
                    "animation_frame"
                ]
            }
        }
    ]
    return functions

def helper_agent(api_key, input_code):
    agent = TracerAgent(api_key)
    
    helper_prompt = "You are a helper agent. Your goal is to semantically explain input code in plain English. Point out any bugs, errors, data structures, loops, recursion, and general behavior. Then your explanations will be used for another agent to visualize the input code's behavior" + prompt
    
    config = types.GenerateContentConfig(
        system_instruction = helper_prompt,
        temperature=0.1,
    )
    input_code = str(input_code)
    contents = types.Content(role="user", parts = [types.Part(text=input_code)])
    
    response = agent.trace(contents, config, model = "gemini-2.0-flash-lite")
    
    file_path = r"Agentic_AI\LLM_Files\recommendations.txt"
    with open(file_path, "w") as file:
        file.write(response.text)
    
    return response.text
        


def gemini_tracer(api_key, input_code):
    backup_input = helper_agent(api_key, input)
    
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
        temperature=0.1
    )

    input = str(function_calls) + str(input_code)
    contents = types.Content(role="user", parts=[types.Part(text=input)])

    response = BackUp.trace(contents, config, model="gemini-2.0-flash-lite")
    file_path = r"Agentic_AI\LLM_Files\logic_tweaks.txt"


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
