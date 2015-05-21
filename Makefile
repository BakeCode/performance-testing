test:
	nosetests tests/

watch:
	watchmedo shell-command --patterns="*.py" --recursive --command='make test'
run:
	./run.py
