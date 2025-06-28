from google.genai import types
from Agentic_AI.base_agent import TracerAgent


code_path = r"Agentic_AI\LLM_Files\test_case1.txt"
with open(code_path, "r") as file:
    input_code = file.read()

prompt_path = r"Agentic_AI\LLM_Files\system_prompt.txt"
with open(prompt_path, "r") as file:
    prompt = file.read()


def declare_functions():
    functions = [
        {
            "name": "draw_text",
            "description": "DESCRIBE DRAW TEXT",
            "parameters": 
            {
                "type": "object",
                "properties": {

                    "text": {
                        "type": "string",
                        "description": "DESCRIPTION",
                        "maxLength": 2

                    },

                    "coordinates": {
                        "type": "array",
                        "description": "(X,Y) coordinates description",
                        "items": {"type": "number"},
                        "minItems": 2,
                        "maxItems": 2
                    },

                    "font_size": {
                        "type": "number",
                        "description": "Size of your text",
                    },

                    "animation_frame": 
                    {
                        "type": "number",
                        "description": "You can group drawings into frames! Sequentially group your drawings together to visualize each line of code",
                        "minimum":0,
                        "maximum": 20,
                    },

                },

                "required": ["text", "coordinates", "font_size", "animation_frame"],
            },
        },   
    ]
    return functions


def gemini_tracer(api_key):
    drawing_tools = types.Tool(function_declarations=declare_functions())

    config = types.GenerateContentConfig(
        system_instruction=prompt,
        temperature=1.7,
        tools=[drawing_tools],
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False), #These are helpful according to the documentation
        tool_config=types.ToolConfig(function_calling_config=types.FunctionCallingConfig(mode='ANY')),
        )

    agent = TracerAgent(api_key)

    response = agent.trace(
        contents=input_code,
        config=config,
    )

    return response.function_calls

if __name__ == '__main__':
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_key = os.getenv("GEMINI_KEY")

    print(gemini_tracer(api_key))
