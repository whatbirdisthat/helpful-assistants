include scripts/vllm-openai.mak
include scripts/vllm-endpoint.mak
include scripts/tgi.mak


THIS_IP := $(shell ip -4 addr show eno1 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')

what-is-my-ip:
	@echo "THIS IP "$(THIS_IP)


watch-running:
	cat vllm-service-*.log | gum table -p

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

run:
	OPENAI_ORGANISATION=$$(pass openai/organisation) \
	OPENAI_API_KEY=$$(pass openai/api-key) \
	python app.py


test-mode:
	python app.py -t

unit-test:
	python -m unittest ./**/*.py


.PHONY: run test
