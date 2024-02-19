import os
from vllm import LLM, SamplingParams


class VllmClient:
    base_folder = "/media/user/4T_RAID/AIs/MODELS/LANGUAGE_MODELS/MODELS"
    models_that_work = [
        "facebook/opt-125m",
        "Wizard-Vicuna-13B-Uncensored-GPTQ",
        "Llama-2-13b-hf"
    ]

    def __init__(self):
        self.sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
        model_backend = 2
        model_identifier = f'{self.models_that_work[model_backend]}'
        loading_from_hub = '/' in model_identifier
        if not loading_from_hub:
            model_identifier = f'{self.base_folder}/{self.models_that_work[model_backend]}'
        self.llm = LLM(
            model=model_identifier,
            tensor_parallel_size=2,
            gpu_memory_utilization=0.75
        )

    def send_content(self, model, message, system_message):
        """
        Fake method to use instead of the openai client's method
        :param message: any message
        :return: response:obj, content:str
        """
        # sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
        # # llm = LLM(model="facebook/opt-125m")
        # llm = LLM(
        #     model="/media/user/4T_RAID/AIs/MODELS/Wizard-Vicuna-13B-Uncensored-GPTQ",
        #     tensor_parallel_size=2,
        #
        # )
        PRE_PROMPT=f'<|im_start|>system\n{system_message}'
        USER_PROMPT=f'<|im_end|>\n<|im_start|>user\n{message}'
        POST_PROMPT='<|im_end|>\n<|im_start|>assistant\n'


        outputs = self.llm.generate(
            prompts=[message],
            sampling_params=self.sampling_params)
        response = ""
        for output in outputs:
            response = output.outputs[0].text
            print(output.outputs[0].text)

        return outputs, response
