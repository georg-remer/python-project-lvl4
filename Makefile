setup: copy-env install migrate

copy-env:
	cp -n .env.example .env

install:
	poetry install

selfcheck:
	poetry check

lint:
	poetry run flake8 task_manager

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run --source='.' manage.py test task_manager
	coverage html
	coverage report

check: selfcheck lint

prepare-requirements:
	poetry export -f requirements.txt --output requirements.txt

prepare-migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

run:
	poetry run python manage.py runserver 0.0.0.0:8000

run-gunicorn:
	poetry run gunicorn task_manager.wsgi

update-locale:
	poetry run django-admin makemessages --locale ru

compile-locale:
	poetry run django-admin compilemessages