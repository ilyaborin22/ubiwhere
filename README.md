

- There are no tests as there were no requirements for that
- In order to populate the DB, need to run the custom command (implemented in management/commands/populate_db.py):
    python3 manage.py populate_db
heroku run python manage.py populate_db