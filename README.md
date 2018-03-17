# Beesh

Beesh is a web based tool for beekeepers.


## Environment Variables

- `BEESH_SECRET_KEY` -- Defaults to a randomly generated key
- `BEESH_DEBUG -- Set to anything to enable debugging. Defaults to `False`
- `BEESH_HOSTNAMES` -- Add hostnames to `ALLOWED_HOSTS`. List of hosts separated with `,`, e. g. `beesh.com,localhost`
- `DATABASE_URL` -- Set a database URL, e. g. `postgres://user:password@localhost:5432/beesh`. Defaults to sqlite.