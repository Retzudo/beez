# Beez

Beez is a web based tool for beekeepers.


## Environment Variables

- `BEEZ_SECRET_KEY` -- Defaults to a randomly generated key
- `BEEZ_DEBUG -- Set to anything to enable debugging. Defaults to `False`
- `BEEZ_HOSTNAMES` -- Add hostnames to `ALLOWED_HOSTS`. List of hosts separated with `,`, e. g. `beez.com,localhost`
- `DATABASE_URL` -- Set a database URL, e. g. `postgres://user:password@localhost:5432/beez`. Defaults to sqlite.