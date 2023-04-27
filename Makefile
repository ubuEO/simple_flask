build:
		docker-compose build

venv: venv/scripts/activate

venv/scripts/activate: requirements.txt
	test -d env || python3.8 -m venv
	. venv/scripts/activate; pip install --upgrade pip; pip install pip-tools wheel -e .; pip-sync requirements.txt requirements-dev.txt
	touch venv/scripts/activate