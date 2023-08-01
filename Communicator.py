import os
import datetime
import openai
from LoggingLogger import LoggingLogger


class Communicator:
    session_filename = None

    def __init__(self):

        the_organisation = os.getenv("OPENAI_ORGANISATION")
        the_api_key = os.getenv("OPENAI_API_KEY")
        if the_organisation is None or the_organisation == "":
            raise EnvironmentError("No OPENAI_ORGANISATION set")
        if the_api_key is None or the_api_key == "":
            raise EnvironmentError("No OPENAI_API_KEY set")
        openai.organization = the_organisation
        openai.api_key = the_api_key

        self.session_filename = f"./chat-logs/log-{datetime.datetime.now():%Y-%m-%d_%H%M}.md"

    def chat_with_llm(self, message, history):
        """
        chat_with_llm is the function we pass to Gradio which implements the signature
        required by the ChatInterface init.
        :param message: The "prompt" message from a "human"
        :param history: All the prompts and responses in a big array
        :return: a str containing the content of the response from ChatGPT (or whatever openai model)
        """
        prompt_object = {
            "prompt": message,
            "history": history
        }
        LoggingLogger.write_json_to_file(prompt_object, self.session_filename)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a business systems expert and analyst"},
                {"role": "user", "content": message}
            ]
        )

        LoggingLogger.write_json_to_file(response, self.session_filename)
        response_content = response.choices[0].message.content
        LoggingLogger.write_interaction_to_file(message, response_content, self.session_filename)
        return response_content
