import os
import openai

from helpers.ArgumentException import ArgumentException


class OpenAiClient:

    def __init__(self):
        the_organisation = os.getenv("OPENAI_ORGANISATION")
        the_api_key = os.getenv("OPENAI_API_KEY")
        if the_organisation is None or the_organisation == "":
            raise EnvironmentError("No OPENAI_ORGANISATION set")
        if the_api_key is None or the_api_key == "":
            raise EnvironmentError("No OPENAI_API_KEY set")
        openai.organization = the_organisation
        openai.api_key = the_api_key

    @staticmethod
    def validate_content(message, system_message):

        if message is None:
            raise ArgumentException("Message is None")

        if system_message is None:
            raise ArgumentException("System message is None")

    def send_content(self,
                     model: str | None,
                     message: str | None = None,
                     system_message: str | None = None,
                     ):
        if model is None:
            model = "gpt-3.5-turbo"

        self.validate_content(message, system_message)

        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": message}
            ]
        )

        return response, response.choices[0].message.content
