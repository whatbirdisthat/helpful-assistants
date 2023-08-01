from datetime import datetime

from helpers.AnnoyingHackJsonConverter import convert_to_json


class LoggingLogger:
    """
    The LoggingLogger is a class I don't think I actually need.
    Being so new to Gradio and all the things, I haven't found a logging thing
    in the framework (yet?).
    Also, I'm not a fan of to-do comments, but:
    TODO: this should be an injected thing (the whole app should use DI/IoC)
    """

    @staticmethod
    def write_json_to_file(input_object: object, filename: str):
        json_data = convert_to_json(input_object)
        print(json_data)

        output = f"""
### {datetime.now().isoformat()}
```json
{json_data}
```

"""

        with open(filename, 'a') as file:
            file.write(output)

    @staticmethod
    def write_interaction_to_file(message: str, response_content: str, filename: str):
        output = f"""
## Interaction

### Prompt:
{message}

### Response
{response_content}

"""
        with open(filename, 'a') as file:
            file.write(output)
