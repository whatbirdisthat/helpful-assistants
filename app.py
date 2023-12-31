"""
app.py
------
The UI for the application.
This is the only part that uses Gradio, which makes the code
less noisy, so I can follow what the code is doing more easily.
From here, we pass the values of the UI components into the
"engine" which uses python primitives.
@Communicator is the class that holds a method we pass to Gradio ChatInterface
and is the easily-swappable piece, so I can write test code that uses a fake
ChatGPT (@FakeCommunicator) and is completely deterministic - a controlled environment.

"""
import argparse

import gradio as gr

from Communicator import Communicator
from helpers.LoggingLogger import LoggingLogger
from clients.OpenAiClient import OpenAiClient
from fakes.FakeOpenAiClient import FakeOpenAiClient

# Acquire configuration from arguments
parser = argparse.ArgumentParser(
    prog='ProgramName',
    description='What the program does',
    epilog='Text at the bottom of help')
parser.add_argument(
    "-t", "--test-mode", action="store_true", required=False,
    help="Use --test-mode to plug in a fake LLM communicator for testing the UI in a deterministic manner"
)
runtime_args = parser.parse_args()

# Declare the components
communicator: Communicator | None = None
app_client: OpenAiClient | FakeOpenAiClient | None = None
app_logger: LoggingLogger = LoggingLogger()

# Inflate the components
if runtime_args.test_mode:
    app_client = FakeOpenAiClient()
else:
    app_client = OpenAiClient()

# Instantiate the Communicator and inject the components
communicator = Communicator(app_client, app_logger)

# Tell Gradio what we want to do
demo = gr.ChatInterface(communicator.chat_with_llm, title="Talk to ChatGPT 📞")

if __name__ == "__main__":
    demo.launch()
