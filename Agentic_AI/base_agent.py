from google import genai


class TracerAgent():
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def trace(self, contents, config, model):

        self.response = self.client.models.generate_content(
            model=model,
            contents=contents,
            config=config
        )

        return self.response

