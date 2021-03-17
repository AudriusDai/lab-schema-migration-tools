# alembic
## Startup commands

```
docker-compose up --build
python3 -m venv env
. env/bin/activate
python3 -m pip install -r requirements.txt
```

## Usage
Create a version with message:
```
cd migrator-src
alembic revision -m "create account table"
```

Versions are referenced via `down_revision` variable.

Can manually add some commands to `upgrade` or `downgrade` methods.

Run migrations:
```
alembic upgrade head
```

Table was created via scripts. Also there is additional table `alembic_version` to track short-keys of the executed version scripts.

## Helping notes
```
pip freeze > requirements.txt
```
Source of docs https://alembic.sqlalchemy.org/en/latest/front.html

How to set sqlalchemy.url from env variables https://stackoverflow.com/questions/37890284/ini-file-load-environment-variable