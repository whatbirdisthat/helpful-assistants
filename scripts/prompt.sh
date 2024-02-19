#DEFAULT_MODEL=dolphin-2.2.1-mistral-7b
#DEFAULT_MODEL=Llama-2-13b-hf
#DEFAULT_MODEL=Llama-2-13b-chat-hf
#DEFAULT_MODEL=mosaicml_mpt-7b-chat
#DEFAULT_MODEL=mixtral-7B-8expert-GPTQ
MODELS_FOLDER=/media/user/4T_RAID/AIs/MODELS/LANGUAGE_MODELS/MODELS

AVAILABLE_MODELS=$(ls ${MODELS_FOLDER})

RUNNING_MODELS=$(cat vllm-service-*.log | awk -F, '{ print $1 }')

THIS_MODEL=$(gum choose ${RUNNING_MODELS})

THIS_IP=$(ip -4 addr show eno1 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
THIS_PORT=$(gum choose 8000 8001 8002 8003)

TEST_PROMPT_1="Write a brief poem in the style of the Romantic Poets (Byron, Coleridge, Shelley) about a fine ship on a stormy sea that is consumed by the Kraken. Format the poem as Markdown text."
TEST_PROMPT_2="The three most common vowels are"
CHOICE_CUSTOM=CUSTOM...
TEST_PROMPT=$(gum choose "${TEST_PROMPT_1}" "${TEST_PROMPT_2}" "${CHOICE_CUSTOM}")

if [ "${CHOICE_CUSTOM}" == "${TEST_PROMPT}" ]; then
	#THIS_GPU_ALLOC=$(gum input --value="0.85" --char-limit=6 --placeholder="Decimal between 0.0 and 1.0" --prompt="Allocate VRAM GBs 🔀 ")
	TEST_PROMPT=$(gum input --prompt="Enter prompt: " --value="${TEST_PROMPT_2}" --char-limit=64)
fi

TEST_SYSTEM_PROMPT="You (ASSISTANT) are a master poet. When asked, you write the most beautiful poems depicting the story your Patron has asked for. You make use of the Markdown formatting for the poem's textual elements."

THIS_TEMPERATURE=$(gum input --char-limit=4 --value="1.0" --prompt="Temperature: ")

#define TEST_HTTPIE_ORIG
#echo '{"model":"$(DEFAULT_MODEL)","messages":[{"role": "user", "content": "$(TEST_PROMPT)"},{"role":"assistant","content":"$(TEST_SYSTEM_PROMPT)"}]}' | http -j http://$(THIS_IP):8000/v1/chat/completions -b
#endef
#	@$(TEST_HTTPIE)
#	@$(TEST_HTTPIE) | jq -r '.choices[].message.content' | gum format -t markdown

#TEST_JSON="{\"model\":\"${THIS_MODEL}\",\"messages\":[{\"role\": \"user\", \"content\": \"${TEST_PROMPT}\"},{\"role\":\"assistant\",\"content\":\"${TEST_SYSTEM_PROMPT}\"}]}"
TEST_JSON="{
  \"model\":  \"${THIS_MODEL}\",
  \"temperature\":  \"${THIS_TEMPERATURE}\",
  \"messages\": [{
    \"role\": \"user\",
    \"content\":  \"${TEST_PROMPT}\"
  },{
  \"role\": \"assistant\",
  \"content\":  \"${TEST_SYSTEM_PROMPT}\"
  }]
}"

echo ${TEST_JSON} |
	http -jb http://${THIS_IP}:${THIS_PORT}/v1/chat/completions |
	jq -r '.choices[].message.content' |
	gum format -t markdown &&
	echo "### ${THIS_MODEL}" |
	gum format -t markdown
