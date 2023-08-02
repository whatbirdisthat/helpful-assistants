from helpers.LoggingLogger import LoggingLogger


class Communicator:
    """
    The Communicator class is where all the inputs and outputs are marshalled.
    """
    logger: LoggingLogger | None = None
    model: str = "gpt-3.5-turbo"
    system_message = "You are a business systems expert and analyst"

    def __init__(self, client, logger: LoggingLogger):
        self.openai_client = client
        self.logger = logger

    def chat_with_llm(self, message, history):
        """
        chat_with_llm is the function we pass to Gradio which implements the signature
        required by the ChatInterface init.
        :param message: The "prompt" message from a "human"
        :param history: All the prompts and responses in a big array
        :return: a str containing the content of the response from ChatGPT (or whatever openai model)
        """
        prompt_object = {
            "human": message,
            "system": self.system_message,
            "history": history
        }
        self.logger.write_json_to_file(prompt_object)

        response, response_content = self.openai_client.send_content(
            self.model,
            message,
            self.system_message
        )

        self.logger.write_json_to_file(response)
        self.logger.write_interaction_to_file(message, response_content)

        return response_content
