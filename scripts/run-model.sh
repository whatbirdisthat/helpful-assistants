#!/usr/bin/env bash
#

MODELS_FOLDER=/media/user/4T_RAID/AIs/MODELS/LANGUAGE_MODELS/MODELS

AVAILABLE_MODELS=$(ls ${MODELS_FOLDER})
THIS_IP=$(ip -4 addr show eno1 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')

echo '
# Choose from a list of models.
---
' | gum format -t markdown

THIS_MODEL=$(gum filter ${AVAILABLE_MODELS})
THIS_PORT=$(gum choose 8000 8001 8002 8003)
THIS_GPUS=$(gum choose "0" "1" "0,1")
THIS_GPU_ALLOC=$(gum input --value="0.85" --char-limit=6 --placeholder="Decimal between 0.0 and 1.0" --prompt="Allocate VRAM GBs 🔀 ")
THIS_PARALLEL_SIZE=1
if [ "0,1" == "${THIS_GPUS}" ]; then
	THIS_PARALLEL_SIZE=2
fi

echo "MODELS_FOLDER: ${MODELS_FOLDER}"
echo "# ${THIS_MODEL} (${THIS_IP}:${THIS_PORT})
_using ${THIS_GPU_ALLOC} of ${THIS_PARALLEL_SIZE} GPUs_" | gum format -t markdown

echo "Model, Host, GPU, %, #
${THIS_MODEL},\"${THIS_IP}:${THIS_PORT}\",${THIS_GPUS},\"${THIS_GPU_ALLOC}\",${THIS_PARALLEL_SIZE}" >vllm-service-${THIS_PORT}.log

NCCL_P2P_DISABLE=1 CUDA_VISIBLE_DEVICES=${THIS_GPUS} \
	conda run \
	--cwd=/home/user/Code/wbit/helpful-assistants/ \
	--live-stream \
	-n helpful-assistants \
	python -m vllm.entrypoints.openai.api_server \
	--model ${MODELS_FOLDER}/${THIS_MODEL} \
	--host ${THIS_IP} \
	--port ${THIS_PORT} \
	--gpu-memory-utilization ${THIS_GPU_ALLOC} \
	--tensor-parallel-size ${THIS_PARALLEL_SIZE} \
	--dtype float16 \
	--disable-log-stats \
	--max-model-len 512 \
	--served-model-name ${THIS_MODEL}

#INFO 02-19 13:02:13 llm_engine.py:337] # GPU blocks: 2467, # CPU blocks: 4096                                  │
