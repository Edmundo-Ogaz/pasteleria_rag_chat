env:
	python3 -m venv venv

activate:
	source venv/bin/activate

run:
	chainlit run app.py -w