import os
import gradio as gr
import openai

the_organisation = os.getenv("OPENAI_ORGANISATION")
the_api_key = os.getenv("OPENAI_API_KEY")
if the_organisation is None or the_organisation == "":
    raise EnvironmentError("No OPENAI_ORGANISATION set")
if the_api_key is None or the_api_key == "":
    raise EnvironmentError("No OPENAI_API_KEY set")
openai.organization = the_organisation
openai.api_key = the_api_key


def chat_with_openai(message, history):
    z = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a business systems expert and analyst"},
            {"role": "user", "content": message}
        ]
    )
    return z.choices[0].message.content


demo = gr.ChatInterface(chat_with_openai, title="Talk to ChatGPT 📞")

if __name__ == "__main__":
    demo.launch()
