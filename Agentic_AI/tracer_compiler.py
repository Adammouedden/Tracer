from agent import gemini_tracer
import shapes

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
                text = fn.args["text"]
                coordinates = fn.args["coordinates"]
                font_size = fn.args["font_size"]
                shapes.draw_text(surface, text, coordinates, font_size)
                
            case "draw_node":
                return

            case "draw_arrow":
                return

if __name__ == "__main__":
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_key = os.getenv("GEMINI_KEY")