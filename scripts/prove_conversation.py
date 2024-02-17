from gradio_client import Client

PROMPT = '''
make a list of the things you see. do not explain why you see them.
do explain what they are doing. do explain where they are.
do not say anything other than the list of things you see.
When I provide the list
cat,cat,cow,rock,rock,airplane
what do you see -
do not simply repeat the list,
but describe what you see in your mind.

'''.replace("\n", " ").replace('\t', ' ').replace("  ", " ")

client = Client("http://192.168.1.15:7860/")

result = client.predict(
    PROMPT,  # str in 'parameter_6' Textbox component
    api_name="/chat"
)
print(result)
