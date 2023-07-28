import json
from datetime import datetime


class LoggingLogger:

    @staticmethod
    def write_json_to_file(input_object: object, filename: str):
        json_data = json.dumps(input_object, indent=4)
        print(json_data)

        with open(filename, 'a') as file:
            file.write('\n')
            file.write(f'## {datetime.now().isoformat()}\n')
            file.write('\n```json\n')
            file.write(json_data)
            file.write('\n```\n')

    @staticmethod
    def write_interaction_to_file(message: str, response_content: str, filename: str):
        with open(filename, 'a') as file:
            file.write('\n')
            file.write(f'## Interaction\n')
            file.write('\n### Prompt:\n')
            file.write(message)
            file.write('\n### Response\n')
            file.write(response_content)
            file.write('\n\n')
