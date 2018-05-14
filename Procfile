web: gunicorn --chdir beez beez.wsgi --log-file=-
release: python beez/manage.py collectstatic --no-input && python beez/manage.py migrate