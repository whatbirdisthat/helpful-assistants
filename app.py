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
from clients.VllmClient import VllmClient
from helpers.LoggingLogger import LoggingLogger
from clients.OpenAiClient import OpenAiClient
from fakes.FakeOpenAiClient import FakeOpenAiClient
from helpers.AssistantDefinitions import AssistantDefinitions

# Acquire configuration from arguments
parser = argparse.ArgumentParser(
    prog='ProgramName',
    description='What the program does',
    epilog='Text at the bottom of help')
parser.add_argument(
    "-t", "--test-mode", action="store_true", required=False,
    help="Use --test-mode to plug in a fake LLM communicator for testing the UI in a deterministic manner"
)
parser.add_argument(
    "-l", "--local-mode", action="store_true", required=False,
    help="Use --local-mode to plug in a local vLLM communicator"
)
parser.add_argument(
    "-s", "--server-name", required=False, default="localhost",
    help="The name of the server to listen, defaults to loopback (localhost) for security."
)
runtime_args = parser.parse_args()

# Declare the components
communicator: Communicator | None = None
app_client: OpenAiClient | FakeOpenAiClient | VllmClient | None = None
app_logger: LoggingLogger = LoggingLogger()

assistant_definitions = AssistantDefinitions()

# Inflate the components
if runtime_args.local_mode:
    app_client = VllmClient()
else:
    if runtime_args.test_mode:
        app_client = FakeOpenAiClient()
    else:
        app_client = OpenAiClient()

# Instantiate the Communicator and inject the components
communicator = Communicator(app_client, app_logger, assistant_definitions)


def radio_changed(radio_value):
    if radio_value is None:
        radio_value = communicator.assistant_definitions[0]
    print(f"radio_value: {radio_value}")
    communicator.set_assistant(radio_value)
    # communicator.assistant = radio_value
    return radio_value


def model_changed(model_value):
    if model_value is None:
        model_value = "openai"
    print(f"model_value: {model_value}")
    communicator.model = model_value
    return model_value


# the_assistants = ["SCIENCE", "ART", "BUSINESS", "POLITICS", "PHILOSOPHY", "HISTORY", "LITERATURE", "MUSIC", "SPORTS",
#                   "GAMING", "MOVIES"]
#
# communicator.assistant = the_assistants[0]
css = """
#component-13 {
    height: 600px; !important
}
"""

with gr.Blocks(title="🐬 Cyberdolphin API 🐬", css=css) as base_interface:
    with gr.Row():
        gr.Label("🐬 Cyberdolphin API 🐬")
    with gr.Row():
        col1 = gr.Column(scale=1)
        with col1:
            model_dropdown = gr.Dropdown(
                choices=["openai", "vllm"], value="openai", interactive=True,
                label="Engine", show_label=True,
                info="The engine to use")
            model_dropdown.change(fn=model_changed, inputs=model_dropdown)
            gr.Markdown("## Assistant")
            assistant_radio = gr.Radio(
                communicator.assistant_definitions, elem_classes="radio-group", label="Assistant", show_label=True,
                value=communicator.assistant_definitions[0], interactive=True,
                info="""The assistant to use. Each assistant is a specialised SYSTEM prompt."""
            )
            assistant_radio.change(fn=radio_changed, inputs=assistant_radio)

        with gr.Column(scale=4) as col2:
            chatinterface = gr.ChatInterface(communicator.chat_with_llm, css=css)

if __name__ == "__main__":
    base_interface.launch(server_name=runtime_args.server_name)
    # demo.launch(server_name=runtime_args.server_name)
