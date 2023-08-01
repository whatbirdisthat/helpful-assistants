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
from fakes.FakeCommunicator import FakeCommunicator

communicator: Communicator | FakeCommunicator | None = None
parser = argparse.ArgumentParser(
    prog='ProgramName',
    description='What the program does',
    epilog='Text at the bottom of help')
parser.add_argument(
    "-t", "--test-mode", action="store_true", required=False,
    help="Use --test-mode to plug in a fake LLM communicator for testing the UI in a deterministic manner"
)
runtime_args = parser.parse_args()

if runtime_args.test_mode:
    communicator = FakeCommunicator()
else:
    communicator = Communicator()

demo = gr.ChatInterface(communicator.chat_with_llm, title="Talk to ChatGPT 📞")

if __name__ == "__main__":
    demo.launch()
