

vllm-mpt-7b:
	conda run \
		--cwd=/home/user/Code/wbit/helpful-assistants/ \
		--live-stream \
		-n helpful-assistants \
		python -m vllm.entrypoints.api_server \
		--host $(THIS_IP) \
		--model /media/user/4T_RAID/AIs/MODELS/LANGUAGE_MODELS/MODELS/mosaicml_mpt-7b-chat \
		--tensor-parallel-size 2

vllm-llama-13b:
	conda run \
		--cwd=/home/user/Code/wbit/helpful-assistants/ \
		--live-stream \
		-n helpful-assistants \
		python -m vllm.entrypoints.api_server \
		--host $(THIS_IP) \
		--model /media/user/4T_RAID/AIs/MODELS/LANGUAGE_MODELS/MODELS/Llama-2-13b-hf \
		--tensor-parallel-size 2


# The "cool prompt" for proof

define COOL_PROMPT_1
make a list of the things you see, do not explain why you see them, do not say anything other than the list of things you see. When I provide the list cat,cat,cow,rock,rock,airplane what do you see - do not simply repeat the list
endef
export COOL_PROMPT_1


vllm-generate-list:
	http http://$(THIS_IP):8000/generate --raw '{"prompt": "$(COOL_PROMPT_1)","use_beam_search": false,"n": 1,"temperature": 0.3,"max_tokens":128}'
	@echo

# generate some text
#
vllm-generate:
	@echo
	http http://$(THIS_IP):8000/generate --raw '{"prompt": "cat,rabbit,cow,cow,cow","use_beam_search": false,"n": 1,"temperature": 3.3}'
	@echo



