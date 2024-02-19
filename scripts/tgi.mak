model=facebook/opt-125m
volume="$${PWD}/data"
tgi:
	docker run \
		--gpus all \
		--shm-size 1g \
		-p 8080:80 \
		-v $(volume):/data \
		ghcr.io/huggingface/text-generation-inference:1.1.0 --model-id $(model)



