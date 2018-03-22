FROM python

RUN pip install pipenv

COPY . /beez
RUN cd /beez && pipenv install --system
RUN cd /beez/beez && python manage.py collectstatic --no-input

WORKDIR /beez/beez
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "beez.wsgi", "--log-file=-"]