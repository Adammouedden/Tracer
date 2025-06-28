from google import genai


class TracerAgent():
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def trace(self, contents, config):

        self.response = self.client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=contents,
            config=config
        )

        return self.response
