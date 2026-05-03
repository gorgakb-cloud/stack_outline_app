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

1. Create and activate a virtual environment.
   ```
   python -m venv venv   
   venv\Scripts\activate 
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python run.py
   ```
4. Open http://127.0.0.1:5000

## Notes

- Using MySQL for this project instead of SQLite
- Professor signed off on normalization/schema changes
- Normalization report can be found in NORMALIZATION.md
- If the local webserver doesnt come up when you run run.py, make sure you are cd-ed into the right directory (stack_outline_app)

