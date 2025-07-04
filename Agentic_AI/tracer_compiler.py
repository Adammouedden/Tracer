from Agentic_AI.agent import gemini_tracer, double_check, max_frames
import shapes
import configs as cfg
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_KEY")


def build_animation_frames(input_code):
    functions = gemini_tracer(api_key, input_code)
    #initial_functions = str(initial_functions)
    #functions = double_check(api_key, input_code, initial_functions)
    
    animation_frames = [[] for _ in range(max_frames + 1)]
    frame_index = 0

    for fn in functions:
        frame_index = fn.args['animation_frame']
        animation_frames[frame_index].append(fn)
    
    return animation_frames


def parse_function_calls(viz_surface, text_surface, frame):
    if frame == None or frame == 0:
        return
    text_count = 0
    for fn in frame:
        match fn.name:
            case "draw_text" if text_count < 1:
                text = fn.args["text"] 
                coordinates = fn.args["coordinates"]
                coordinates = (0,0)
                font_size = fn.args["font_size"]
                shapes.draw_text(text_surface, text, coordinates, font_size, color = cfg.WHITE)
                text_count += 1
                
                
            case "draw_node":
                value = fn.args["value"]
                coordinates = fn.args["coordinates"]
                rectangle_width = fn.args["rectangle_width"]
                rectangle_height = fn.args["rectangle_height"]
                error = fn.args["error"]
                highlight = fn.args["highlight"]
                shapes.draw_node(viz_surface, value, coordinates, rectangle_width, rectangle_height, error, highlight)

            case "draw_arrow":
                start_pos = fn.args["start_pos"]
                end_pos = fn.args["end_pos"]
                shapes.draw_arrow(viz_surface, start_pos, end_pos)

            case "draw_circular_node":
                value = fn.args["value"]
                center = fn.args["center"]
                radius = fn.args["radius"]
                shapes.draw_circular_node(viz_surface, value, center, radius)


   