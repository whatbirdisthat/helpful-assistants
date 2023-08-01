import datetime
from fakes.FakeResponse import create_fake_response
from LoggingLogger import LoggingLogger


class FakeCommunicator:
    session_filename = None

    def __init__(self):
        self.session_filename = f"./chat-logs/log-{datetime.datetime.now():%Y-%m-%d_%H%M}.md"

    def chat_with_llm(self, message, history):
        prompt_object = {
            "prompt": message,
            "history": history
        }
        LoggingLogger.write_json_to_file(prompt_object, self.session_filename)
        response = create_fake_response()
        LoggingLogger.write_json_to_file(response, self.session_filename)
        response_content = response.choices[0].message.content
        LoggingLogger.write_interaction_to_file(message, response_content, self.session_filename)
        return response_content
