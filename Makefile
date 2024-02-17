model=facebook/opt-125m
volume="$${PWD}/data"
THIS_IP := $(shell ip -4 addr show eno1 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')

what-is-my-ip:
	@echo "THIS IP "$(THIS_IP)

openai:
	conda run \
		--cwd=/home/user/Code/wbit/helpful-assistants/ \
		--live-stream \
		-n helpful-assistants \
		python -m vllm.entrypoints.openai.api_server \
		--model /media/user/4T_RAID/AIs/MODELS/LANGUAGE_MODELS/MODELS/mosaicml_mpt-7b-chat \
		--swap-space 50 \
		--gpu-memory-utilization 0.85 \
		--tensor-parallel-size 1 \
		--served-model-name mosaicml_mpt-7b-chat

# cuda-device 1 is unrecognised argument
#		--cuda-device 1 \

openai-device-1-no-longer-working:
	conda run \
		--cwd=/home/user/Code/wbit/helpful-assistants/ \
		--live-stream \
		-n helpful-assistants \
		python -m vllm.entrypoints.openai.api_server \
		--host $(THIS_IP) \
		--model /media/user/4T_RAID/AIs/MODELS/LANGUAGE_MODELS/MODELS/mosaicml_mpt-7b-chat \
		--swap-space 40 \
		--gpu-memory-utilization 0.95 \
		--tensor-parallel-size 1 \
		--served-model-name mosaicml_mpt-7b-chat

openai-device-1:
	conda run \
		--cwd=/home/user/Code/wbit/helpful-assistants/ \
		--live-stream \
		-n helpful-assistants \
		python -m vllm.entrypoints.openai.api_server \
		--host $(THIS_IP) \
		--model /media/user/4T_RAID/AIs/MODELS/LANGUAGE_MODELS/MODELS/mosaicml_mpt-7b-chat \
		--swap-space 40 \
		--gpu-memory-utilization 0.95 \
		--tensor-parallel-size 1 \
		--cuda-device 1 \
		--served-model-name mosaicml_mpt-7b-chat

openai-llama2-13b-chat:
	conda run \
		--cwd=/home/user/Code/wbit/helpful-assistants/ \
		--live-stream \
		-n helpful-assistants \
		python -m vllm.entrypoints.openai.api_server \
		--host $(THIS_IP) \
		--model /media/user/4T_RAID/AIs/MODELS/LANGUAGE_MODELS/MODELS/Llama-2-13b-chat-hf \
		--tensor-parallel-size 2 \
		--served-model-name Llama-2-13b-chat-hf

openai-neural-chat-7b:
	conda run \
		--cwd=/home/user/Code/wbit/helpful-assistants/ \
		--live-stream \
		-n helpful-assistants \
		python -m vllm.entrypoints.openai.api_server \
		--host 127.0.0.1 \
		--model /media/user/4T_RAID/AIs/MODELS/LANGUAGE_MODELS/MODELS/neural-chat-7B-v3-1-AWQ \
		--tensor-parallel-size 2 \
		--quantization awq \
		--dtype auto \
		--served-model-name neural-chat-7B-v3-1-AWQ


vllm:
	conda run \
		--cwd=/home/user/Code/wbit/helpful-assistants/ \
		--live-stream \
		-n helpful-assistants \
		python -m vllm.entrypoints.api_server \
		--host $(THIS_IP) \
		--model /media/user/4T_RAID/AIs/MODELS/LANGUAGE_MODELS/MODELS/mosaicml_mpt-7b-chat \
		--tensor-parallel-size 2

vllm-llama:
	conda run \
		--cwd=/home/user/Code/wbit/helpful-assistants/ \
		--live-stream \
		-n helpful-assistants \
		python -m vllm.entrypoints.api_server \
		--host $(THIS_IP) \
		--model /media/user/4T_RAID/AIs/MODELS/LANGUAGE_MODELS/MODELS/Llama-2-13b-hf \
		--tensor-parallel-size 2

gradio:
	OPENAI_ORGANISATION=FAKE_OPENAI_ORG \
	OPENAI_API_KEY=FAKE_OPENAI_KEY \
	OPENAI_API_URL=http://$(THIS_IP):8000 \
	conda run \
		--cwd=/home/user/Code/wbit/helpful-assistants/ \
		--live-stream \
		-n helpful-assistants \
		python app.py \
		--server-name $(THIS_IP)

define COOL_PROMPT_1
make a list of the things you see, do not explain why you see them, do not say anything other than the list of things you see. When I provide the list cat,cat,cow,rock,rock,airplane what do you see - do not simply repeat the list
endef
export COOL_PROMPT_1

vllm-generate-list:
	http http://$(THIS_IP):8000/generate --raw \
'{"prompt": "$(COOL_PROMPT_1)","use_beam_search": false,"n": 1,"temperature": 0.3,"max_tokens":128}'

vllm-generate:
	http http://$(THIS_IP):8000/generate --raw \
'{"prompt": "cat,rabbit,cow,cow,cow","use_beam_search": false,"n": 1,"temperature": 3.3}'

tgi:
	docker run \
		--gpus all \
		--shm-size 1g \
		-p 8080:80 \
		-v $(volume):/data \
		ghcr.io/huggingface/text-generation-inference:1.1.0 --model-id $(model)


run:
	OPENAI_ORGANISATION=$$(pass openai/organisation) \
	OPENAI_API_KEY=$$(pass openai/api-key) \
	python app.py

test-mode:
	python app.py -t

unit-test:
	#python -m unittest ./**/*.py
	python -m unittest ./**/*.py

.PHONY: run test
