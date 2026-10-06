# DBAmbi
Following a fast api tutorial on youtube, will eventually use
as framework to create query interface with salesforce environments

## console commands

- add package:
  - uv add pandas
  - uv add fastapi
  - uv add simple_salesforce
### run app
  - uv run fastapi dev main.py
### generate mock data in database
  - uv run python populate_db.py
### create secret_key in terminal
  - python -c "import secrets; print(secrets.token_hex(32))"
### Postgres commands
  - psql -U postgres
    - access command line
  - psql -U postgres -c "CREATE USER bloguser WITH PASSWORD 'blogpass';"
  - createdb -U postgres -O bloguser blog
  - createdb -U postgres -O bloguser test_blog
### postgres command line:
  - \l - list all database
  - \c <dbname> connect to specific db
  - \dt list all table in current database
  - \d <tablename> describe table, columns, datatypes, indexes...
  - \dn list all schemas on db
  - \dv list all views on db
  - \du list all users and privileges
  - \dx	List installed extensions.
  - \q quit out of postgres terminal
  - \i filename.sql	Execute an SQL file directly from inside the session.
### Run alembic for database setup/migration
  - uv run alembic init -t async alembic
  - uv run alembic revision --autogenerate -m "initial schema"
    - --autogenerate creates migration file, but does not execute it
  - uv run alembic upgrade head
    - update migrations based on latest version in version folder
    - (this is the execution of migration file)
  - uv run alembic current
    - check state on latest alembic migration
  - uv run alembic downgrade -1
    - go back one migration
### pytest commands
  - uv run pytest tests/test_posts.py -v
  - uv run pytest tests/test_users.py -v
  - uv run pytest tests/ -v
  - uv run pytest tests/
  - uv run pytest tests/test_posts.py::test_get_posts_empty -v

## mailtrap.io  
Use mailtrap.io to test reset_passowrd attempts so as to not accidentally send spam email password reset request to real emails.

## Docker
 - docker build -t fastapi-app .
 - docker run -p 8080:8080 --env-file .env fastapi-app
## Google Cloud Run
 - gcloud --version
 - gcloud auth login
 - gcloud config set project fastapi-blog-510805
 - gcloud services enable run.googleapis.com
 - gcloud services enable cloudbuild.googleapis.com
 - gcloud services enable artifactregistry.googleapis.com
 - gcloud services list --enabled
 - gcloud artifacts repositories create fastapi-repo --repository-format=docker --location=us-east4
 - gcloud builds submit --tag us-east4-docker.pkg.dev/fastapi-blog-510805/fastapi-repo/fastapi-app
 - gcloud run deploy fastapi-service --image us-east4-docker.pkg.dev/fastapi-blog-510805/fastapi-repo/fastapi-app --region us-east4 --allow-unauthenticated
