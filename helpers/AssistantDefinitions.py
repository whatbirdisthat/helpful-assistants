import yaml


class AssistantDefinitions:
    # def __init__(self):
    # definitions = yaml.safe_load(open("helpers/assistant-definitions.yaml"))
    # self._assistant_specialisations = definitions["assistant_definitions"]["assistant_specialisations"]
    # self._base_prompt = definitions["assistant_definitions"]["base_prompt"]

    @property
    def definitions(self):
        return yaml.safe_load(open("helpers/assistant-definitions.yaml"))

    @property
    def assistant_specialisations(self):
        return self.definitions["assistant_definitions"]["assistant_specialisations"]

    @property
    def base_prompt(self):
        return self.definitions["assistant_definitions"]["base_prompt"]
