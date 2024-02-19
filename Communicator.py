from helpers.AssistantDefinitions import AssistantDefinitions
from helpers.LoggingLogger import LoggingLogger


class Communicator:
    """
    The Communicator class is where all the inputs and outputs are marshalled.
    """
    logger: LoggingLogger | None = None
    model: str = None
    assistant: str = None

    @property
    def assistant_definitions(self):
        return [a['label'] for a in self._assistant_definitions.assistant_specialisations.values()]

    def set_assistant(self, assistant):
        the_assistant = [(k, a) for k, a in
                         zip(self._assistant_definitions.assistant_specialisations.keys(),
                             self._assistant_definitions.assistant_specialisations.values())
                         if
                         a['label'] == assistant][0]
        self.assistant = the_assistant[0].upper()

    def __init__(self, client, logger: LoggingLogger, assistant_definitions: AssistantDefinitions):
        self.openai_client = client
        self.logger = logger
        self._assistant_definitions = assistant_definitions
        self.assistant = self.assistant_definitions[0]

    def chat_with_llm(self, message, history):
        """
        chat_with_llm is the function we pass to Gradio which implements the signature
        required by the ChatInterface init.
        :param message: The "prompt" message from a "human"
        :param history: All the prompts and responses in a big array
        :return: a str containing the content of the response from ChatGPT (or whatever openai model)
        """
        the_system_prompt = self._assistant_definitions.assistant_specialisations[self.assistant.upper()]["system_prompt"]
        the_system_message = f'{the_system_prompt} {self._assistant_definitions.base_prompt}'

        prompt_object = {
            "human": message,
            "system": the_system_message,
            "history": history
        }
        self.logger.write_json_to_file(prompt_object)

        response, response_content = self.openai_client.send_content(
            self.model,
            message,
            the_system_message
        )

        self.logger.write_json_to_file(response)
        self.logger.write_interaction_to_file(message, response_content)

        return response_content
