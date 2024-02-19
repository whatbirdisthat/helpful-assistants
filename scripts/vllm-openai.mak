MODELS_FOLDER=/media/user/4T_RAID/AIs/MODELS/LANGUAGE_MODELS/MODELS

#DEFAULT_MODEL=dolphin-2.2.1-mistral-7b
#DEFAULT_MODEL=Llama-2-13b-hf
#DEFAULT_MODEL=Llama-2-13b-chat-hf
#DEFAULT_MODEL=mosaicml_mpt-7b-chat
#DEFAULT_MODEL=mixtral-7B-8expert-GPTQ


define TEST_PROMPT
Write a brief poem in the style of the Romantic Poets (Byron, Coleridge, Shelley) about a fine ship on a stormy sea that is consumed by the Kraken. Format the poem as Markdown text.
endef

define TEST_SYSTEM_PROMPT
You (ASSISTANT) are a master poet. When asked, you write the most beautiful poems depicting the story your Patron has asked for. You make use of the Markdown formatting for the poem textual elements.
endef

#define TEST_HTTPIE_ORIG
#echo '{"model":"$(DEFAULT_MODEL)","messages":[{"role": "user", "content": "$(TEST_PROMPT)"},{"role":"assistant","content":"$(TEST_SYSTEM_PROMPT)"}]}' | http -j http://$(THIS_IP):8000/v1/chat/completions -b
#endef
#	@$(TEST_HTTPIE)
#	@$(TEST_HTTPIE) | jq -r '.choices[].message.content' | gum format -t markdown


define TEST_JSON
'{"model":"$(DEFAULT_MODEL)","messages":[{"role": "user", "content": "$(TEST_PROMPT)"},{"role":"assistant","content":"$(TEST_SYSTEM_PROMPT)"}]}'
endef

test-prompt-0:
	echo $(TEST_JSON) | http -j http://$(THIS_IP):8000/v1/chat/completions -b | jq -r '.choices[].message.content' | gum format -t markdown	\
		&& echo '### _SERVER_0_' | gum format -t markdown

test-prompt-1:
	echo $(TEST_JSON) | http -j http://$(THIS_IP):8001/v1/chat/completions -b | jq -r '.choices[].message.content' | gum format -t markdown	\
		&& echo '### _SERVER_1_' | gum format -t markdown

running-models:
	cat ./vllm-service-800*.log

openai:
	conda run \
		--cwd=/home/user/Code/wbit/helpful-assistants/ \
		--live-stream \
		-n helpful-assistants \
		python -m vllm.entrypoints.openai.api_server \
		--model $(MODELS_FOLDER)/$(DEFAULT_MODEL) \
		--host $(THIS_IP) \
		--tensor-parallel-size 2 \
		--served-model-name $(DEFAULT_MODEL)

openai-device-0:
	NCCL_P2P_DISABLE=1 CUDA_VISIBLE_DEVICES=0	\
	conda run \
		--cwd=/home/user/Code/wbit/helpful-assistants/ \
		--live-stream \
		-n helpful-assistants \
		python -m vllm.entrypoints.openai.api_server \
		--host $(THIS_IP) \
		--port 8000	\
		--model $(MODELS_FOLDER)/mosaicml_mpt-7b-chat \
		--tensor-parallel-size 1 \
		--served-model-name mosaicml_mpt-7b-chat	\
		--chat-template scripts/chat-templates/template_chatml.jinja \
		--response-role assistant

openai-device-1:
	NCCL_P2P_DISABLE=1 CUDA_VISIBLE_DEVICES=1	\
	conda run \
		--cwd=/home/user/Code/wbit/helpful-assistants/ \
		--live-stream \
		-n helpful-assistants \
		python -m vllm.entrypoints.openai.api_server \
		--host $(THIS_IP) \
		--port 8001	\
		--tensor-parallel-size 1 \
		--model $(MODELS_FOLDER)/mosaicml_mpt-7b-chat \
		--served-model-name mosaicml_mpt-7b-chat	\
		--chat-template scripts/chat-templates/template_chatml.jinja \
		--response-role assistant

	#	--gpu-memory-utilization 0.85 \



openai-llama2-13b-chat:
	NCCL_P2P_DISABLE=1 CUDA_VISIBLE_DEVICES=0,1	\
	conda run \
		--cwd=/home/user/Code/wbit/helpful-assistants/ \
		--live-stream \
		-n helpful-assistants \
		python -m vllm.entrypoints.openai.api_server \
		--host $(THIS_IP) \
		--model $(MODELS_FOLDER)/Llama-2-13b-chat-hf \
		--tensor-parallel-size 2 \
		--served-model-name Llama-2-13b-chat-hf

openai-neural-chat-7b:
	NCCL_P2P_DISABLE=1 CUDA_VISIBLE_DEVICES=1	\
	conda run \
		--cwd=/home/user/Code/wbit/helpful-assistants/ \
		--live-stream \
		-n helpful-assistants \
		python -m vllm.entrypoints.openai.api_server \
		--host $(THIS_IP) \
		--model $(MODELS_FOLDER)/neural-chat-7B-v3-1-AWQ \
		--tensor-parallel-size 1 \
		--quantization awq \
		--dtype auto \
		--served-model-name neural-chat-7B-v3-1-AWQ

