# Flask-SQLAlchemy Backend

Simple Flask API with SQLAlchemy ORM and Alembic migrations.

## Setup

```bash
pipenv install
pipenv shell
flask db upgrade
python server/seed.py
```

## Run

```bash
python server/app.py
```

Access at http://localhost:5555