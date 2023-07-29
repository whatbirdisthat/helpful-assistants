from datetime import datetime

from AnnoyingHackJsonConverter import convert_to_json


class LoggingLogger:

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
