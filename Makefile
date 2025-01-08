env:
	python3 -m venv venv

activate:
	source venv/bin/activate

run:
	chainlit run app.py -w

nohup:
	nohup python3 -m chainlit run app.py --host 0.0.0.0 --port 80