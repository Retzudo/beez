FROM python

COPY . /beesh
RUN pip install -r /beesh/requirements.txt
RUN cd /beesh/beesh && python manage.py collectstatic --no-input

WORKDIR /beesh/beesh
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "beesh.wsgi", "--log-file=-"]