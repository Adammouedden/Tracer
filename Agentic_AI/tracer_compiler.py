from agent import gemini_tracer
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_KEY")

def build_animation_frames():
    functions = gemini_tracer(api_key)
    
    animation_frames = [[] for i in range(21)]
    frame_index = 0

    for fn in functions:
        frame_index = fn.args['animation_frame']
        animation_frames[frame_index].append(fn)
    
    return animation_frames


def parse_function_calls(surface, frame):
    for fn in frame:
        match fn.name:
            case "draw_text":
                
            case "draw_node":

            case "draw_arrow":

