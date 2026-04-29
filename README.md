# Stack Outline App

Barebones project outline for:
- Python 3
- Flask backend
- Relational DB (SQLite by default)
- SQLAlchemy ORM
- HTML5/CSS3 frontend with Bootstrap and Jinja2 templates
- Git version control

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

## Quick Start

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
