# Stack Outline

- Python 3
- Flask backend
- Relational DB - MySQL
- SQLAlchemy ORM
- HTML5/CSS3 frontend with Bootstrap and Jinja2 templates
- Git version control

# Project Description

Personal assignment tracking app, with functions such as:
- Adding/Deleting/Updating Assignments
- Filtering assignments by class/status
- Adding/Deleting/Updating classes
- Adding/Deleting/Updating professors
- High level overview of assignment count, overdue assignments, and upcoming assignments


## Project Structure

```
stack_outline_app/
  app/
    __init__.py
    extensions.py
    models.py
    routes.py
    static/css/styles.css
    templates/base.html
    templates/index.html
  config.py
  run.py
  requirements.txt
  .env.example
  .gitignore
```

## Installation Instructions
1. Download MariaDB (https://mariadb.org/download/)

2. Run the installer, REMEMBER THE PASSWORD YOU SET
   - This will be used in config.py

3. Navigate to the MariaDB folder on your computer, and open the MariaDB command prompt
   - login via this command (will ask you for your password):
   ```
   mariadb -u root -p
   ```
   - create database:
   ```
   CREATE DATABASE school_tracker;
   EXIT;
   ```
4. Download the .sql file to your computer from this repo, then copy its path
   - Navigate back to MariaDB command prompt
   ```
   -u root -p school_tracker < "COPIED PATH"
   ```
5. Log back into MariaDB again, then run this command:
   ```
   USE school_tracker;
   ```
   - can confirm via SHOW TABLES command

6. Navigate to VSCode stack_outline_app

7. Open config.py, and change the password in the URI to the one youve set. 

8. Create and activate a virtual environment
   ```
   python -m venv .venv   
   .venv\Scripts\activate 
   ```
9. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
10. Run the app:
   ```bash
   python run.py
   ```
11. Open http://127.0.0.1:5000

## Notes

- Using MySQL for this project instead of SQLite
- Professor signed off on normalization/schema changes
- Normalization report can be found in NORMALIZATION.md
- If the local webserver doesnt come up when you run run.py, make sure you are cd-ed into the right directory (stack_outline_app)

