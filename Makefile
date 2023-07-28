run:
	OPENAI_ORGANISATION=$$(pass openai/organisation) \
	OPENAI_API_KEY=$$(pass openai/api-key) \
	python app.py

.PHONY: run
