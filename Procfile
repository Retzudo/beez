web: gunicorn --chdir beez beez.wsgi --log-file=-
release: python beez/manage.py collectstatic && python beez/manage.py migrate