[![Build Status](https://travis-ci.org/Retzudo/beez.svg?branch=master)](https://travis-ci.org/Retzudo/beez)
# Beez

Beez is a web based tool for beekeepers. Written in
[Python](https://python.org/) and powered by [Django](https://djangoproject.com/).

## Deployment

This repository comes with a `Dockerfile` and a `Procfile`. This means
you can build a Docker image and run a container from it or deploy the
app on [Heroku](https://heroku.com/) or your [Dokku](http://dokku.viewdocs.io/dokku/)
installation.


### Docker

The app requires a PostgreSQL database so make sure one is running in
the same Docker network.

1. Create a Docker network or use an existing one.
2. Run a PostgreSQL container.
3. Build an image for with app and run a container while setting the
   necessary environment variables, see below.
4. run `python /beez/beez/manage.py migrate` with `docker exec`.
5. Reverse proxy to the app.


### Dokku/Heroku

1. Create a PostgreSQL database and link it to the app.
2. Make sure `DATABASE_URL` contains the correct connection string.
3. Set the necessary environment variables, see below.
4. Push the code to your Dokku/Heroku remote.


### Regular ol' method

[How to use Django with Gunicorn](https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/gunicorn/).
Beez runs on Python ≥3.5.


## Environment Variables

- `BEEZ_SECRET_KEY` -- Defaults to a randomly generated key.
  I strongly recommend that you set this to something static.
- `BEEZ_DEBUG` -- Django's debugging mode is disabled by default unless this env has any value.
- `BEEZ_HOSTNAMES` -- Add hostnames to `ALLOWED_HOSTS` which is empty by default. List of hosts separated with `,`, e. g. `beez.com,localhost`
- `BEEZ_OWM_API_KEY` -- API key for OpenWeatherMap.
- `DATABASE_URL` -- Set a database URL, e. g. `postgres://user:password@localhost:5432/beez`.
  If this is not set, a local SQLite database file will be used instead.