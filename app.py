import datetime
import os
import gradio as gr
import openai

from FakeResponse import create_fake_response
from LoggingLogger import LoggingLogger

session_filename = f"./chat-logs/log-{datetime.datetime.now():%Y-%m-%d_%H%M}.md"

the_organisation = os.getenv("OPENAI_ORGANISATION")
the_api_key = os.getenv("OPENAI_API_KEY")
if the_organisation is None or the_organisation == "":
    raise EnvironmentError("No OPENAI_ORGANISATION set")
if the_api_key is None or the_api_key == "":
    raise EnvironmentError("No OPENAI_API_KEY set")
openai.organization = the_organisation
openai.api_key = the_api_key


def chat_with_openai(message, history):
    prompt_object = {
        "prompt": message
    }
    LoggingLogger.write_json_to_file(prompt_object, session_filename)
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content": "You are a business systems expert and analyst"},
    #         {"role": "user", "content": message}
    #     ]
    # )
    response = create_fake_response()

    LoggingLogger.write_json_to_file(response, session_filename)
    response_content = response.choices[0].message.content
    LoggingLogger.write_interaction_to_file(message, response_content, session_filename)
    return response_content


demo = gr.ChatInterface(chat_with_openai, title="Talk to ChatGPT 📞")

if __name__ == "__main__":
    demo.launch()
