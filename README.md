# DBAmbi
query data from multiple db and compare on web interface

## console commands

- add package:
  - uv add pandas
  - uv add fastapi
  - uv add simple_salesforce
- run app
  - uv run fastapi dev main.py
- generate mock data in database
  - uv run python populate_db.py
- create secret_key in terminal
  - python -c "import secrets; print(secrets.token_hex(32))"

## mailtrap.io  
Use mailtrap.io to test reset_passowrd attempts so as to not accidentally send spam email password reset request to real emails.
