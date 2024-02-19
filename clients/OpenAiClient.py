import os

import openai
from rich import print
from helpers.ArgumentException import ArgumentException
from openai import OpenAI


class OpenAiClient:

    def __init__(self, url=None):
        the_organisation = os.getenv("OPENAI_ORGANISATION")
        the_api_key = os.getenv("OPENAI_API_KEY")
        the_url = url or os.getenv("OPENAI_API_URL")
        if the_url is not None:
            print(f'Using the url: [green]{the_url}[/]')
            the_organisation = "OPENAI_ORGANISATION"
            the_api_key = "OPENAI_API_KEY"
            # the_models = openai.Model.list(api_base=the_url)
            # self.model = the_models['data'][0].openai_id
            self.model = "this is the model"
            # openai.api_base = the_url
        else:
            if the_organisation is None or the_organisation == "":
                raise EnvironmentError("No OPENAI_ORGANISATION set")
            if the_api_key is None or the_api_key == "":
                raise EnvironmentError("No OPENAI_API_KEY set")

        # openai.organization = the_organisation
        # openai.api_key = the_api_key
        self.the_openai = OpenAI(
            organization=the_organisation,
            api_key=the_api_key,
            base_url=the_url
        )

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
            model = self.model

        self.validate_content(message, system_message)

        response = self.the_openai.chat.completions.create(

            # response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": message}
            ]
        )

        return response, response.choices[0].message.content

    def call_openai_whisper_endpoint(self, audio_filename):
        """
        This method is a placeholder for the real method that will call the OpenAI Whisper endpoint
        :param audio: the audio to send to the OpenAI Whisper endpoint
        :return: the response from the OpenAI Whisper endpoint
        """
        endpoint = self.the_openai
        text = endpoint.audio.transcriptions.create(
            file=audio_filename,
            model="base.en",
            language="en",
            response_format="json",
        )

        return text['text']
