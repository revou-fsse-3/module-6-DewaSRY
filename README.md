<h1>Revou task by <bold>Dewa Surya Ariesta</bold> create simple flask api <h1>

## Requirement to run the project

### Add this on the '.env' and put the '.env' folder on root directory

```bash
FLASK_DEBUG=True
FLASK_APP=src/main.py
FLASK_ENV=development

```

## How to set_up zoo_api

1. set_up Environment - `poetry config virtualenvs.in-project true` // use to make the '.env' on the repo
2. Install all Dependency - `poetry install`
3. set up the environment `poetry shell`
4. run the app -`poetry run flask run`
5. Run Unit Test - `poetry run py -m unittest test`

## To see the swagger ui Document

- in locale `http://127.0.0.1:5000/swagger-ui`
- in production `<YOUR_URL>/swagger-ui`

## data base set up

```bash
//comment to set_up the data base
poetry run flask db

// comment to generate migration to set_up data base
poetry run flask db migrate

// comment to get ready your data base
poetry run flask db upgrade

// comment if you are lazy
poetry run flask db migrate && poetry run flask db upgrade

```

## testing flask
