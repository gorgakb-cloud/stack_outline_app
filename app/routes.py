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
    classes = Class.query.all()
    status = StatusLookup.query.all()
    if request.method == 'POST':
        new_assignment = Assignment(
            Title=request.form['title'],
            Description=request.form['description'],
            CID=request.form['class_name'],
            DueDate=request.form['due_date'],
            SID=request.form['status'],
            Grade=request.form['grade']
        )

        db.session.add(new_assignment)
        db.session.commit()

        return redirect(url_for('main.index'))

   
    return render_template('add_assignment.html', classes=classes, status=status)


@main.route('/add_class', methods=['GET', 'POST'])
def add_class():
    professors = Professor.query.all()

    if request.method == 'POST':
        new_class = Class(
            Title=request.form['title'],
            PID=request.form['professor_id']
        )
        db.session.add(new_class)
        db.session.commit()
        return redirect(url_for('main.index'))
        
    
    return render_template('add_class.html', professors=professors)

@main.route('/add_professor', methods=['GET', 'POST'])
def add_professor():
    if request.method == 'POST':
        new_professor = Professor(
            FullName=request.form['full_name'],
            Email=request.form['email']
        )
        db.session.add(new_professor)
        db.session.commit()
        return redirect(url_for('main.index'))
        
    return render_template('add_professor.html')

@main.route('/delete_professor/<int:PID>')
def delete_professor(PID):
    professor = Professor.query.get_or_404(PID)
    db.session.delete(professor)
    db.session.commit()
    return redirect('/')

@main.route('/delete_class/<int:CID>')
def delete_class(CID):
    class_todelete = Class.query.get_or_404(CID)
    db.session.delete(class_todelete)
    db.session.commit()
    return redirect('/')

@main.route('/delete_assignment/<int:AID>')
def delete_assignment(AID):
    assignment = Assignment.query.get_or_404(AID)
    db.session.delete(assignment)
    db.session.commit()
    return redirect('/')