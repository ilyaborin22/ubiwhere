
- The public website address: https://pacific-basin-32677.herokuapp.com
- The Github repo: https://github.com/ilyaborin22/ubiwhere

Notes:

- In order to populate the DB, need to run the custom command (implemented in management/commands/populate_db.py):
    - python3 manage.py populate_db #locally
    - heroku run python manage.py populate_db # on heroku

- There are no tests as there were no requirements for that
- It doesn't have a quality of a real life product, it's has a level of demo - almost no corner case handling
