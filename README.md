env:
	python3 -m venv venv

activate:
	source venv/bin/activate

run:
	chainlit run app.py -w

pip install chainlit pydantic==2.10.1

test