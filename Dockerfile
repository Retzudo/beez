FROM python

COPY . /beez
RUN pip install -r /beez/requirements.txt
RUN cd /beez/beez && python manage.py collectstatic --no-input

WORKDIR /beez/beez
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "beez.wsgi", "--log-file=-"]