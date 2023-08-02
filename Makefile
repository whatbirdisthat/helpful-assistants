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
