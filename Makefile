run:
	OPENAI_ORGANISATION=$$(pass openai/organisation) \
	OPENAI_API_KEY=$$(pass openai/api-key) \
	python app.py

test:
	python -m unittest ./tests/TestAnnoyingHackJsonConverter.py

.PHONY: run
