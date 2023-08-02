import datetime

from helpers.AnnoyingHackJsonConverter import convert_to_json


class LoggingLogger:
    """
    The LoggingLogger is a class I don't think I actually need.

    Being so new to Gradio and all the things, I haven't found a logging thing
    in the framework (yet?).
    """
    filename: str | None = None

    def __init__(self):
        self.filename = f"./chat-logs/log-{datetime.datetime.now():%Y-%m-%d_%H%M}.md"

    def write_json_to_file(self, input_object: object):
        json_data = convert_to_json(input_object)
        print(json_data)

        output = f"""
### {datetime.datetime.now().isoformat()}
```json
{json_data}
```

"""

        with open(self.filename, 'a') as file:
            file.write(output)

    def write_interaction_to_file(self, message: str, response_content: str):
        output = f"""
## Interaction

### Human:
{message}

### Assistant
{response_content}

"""
        with open(self.filename, 'a') as file:
            file.write(output)
