## Sanic Framework

### Installing dependencies
A mere `pip install sanic` should do.

### Running the app

1. Hypercorn (preferred):
- `$ hypercorn app:app # add --reload for hot reloads`

2. Gunicorn (neccessary to specify worker, else won't work):
- `$ gunicorn app:app --reload --worker-class sanic.worker.GunicornWorker`
