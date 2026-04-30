from datetime import datetime
from flask import Blueprint, render_template, url_for, request, redirect
from .models import Professor, Class, Assignment, StatusLookup
from .extensions import db

main = Blueprint('main', __name__)


@main.route("/")
def index():
    professors = Professor.query.all()
    classes = Class.query.all()
    assignments = Assignment.query.all()
    return render_template("index.html", professors=professors, classes=classes, assignments=assignments)


@main.route('/add_assignment', methods=['GET', 'POST'])
def add_assignment():
    if request.method == 'POST':
        new_assignment = Assignment(
            Title=request.form['title'],
            Description=request.form['description'],
            Class_name=request.form['class_name'],
            DueDate=request.form['due_date'],
            Status=request.form['status'],
            Grade=request.form['grade']
        )

        db.session.add(new_assignment)
        db.session.commit()

        return redirect(url_for('main.index'))

    classes = Class.query.all()
    return render_template('add_assignment.html', classes=classes)


@main.route('/add_class', methods=['GET', 'POST'])
def add_class():
    if request.method == 'POST':
        new_class = Class(
            title=request.form['title'],
            professor_name=request.form['professor_name'],
            assignment_count=request.form['assignment_count']
        )
        db.session.add(new_class)
        db.session.commit()
        return redirect(url_for('main.index'))
        
    professors = Professor.query.all()
    return render_template('add_class.html', professors=professors)