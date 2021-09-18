install:
	poetry install

selfcheck:
	poetry check

lint:
	poetry run flake8 .

check: selfcheck lint

prepare-requirements:
	poetry export -f requirements.txt --output requirements.txt

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