from datetime import datetime
from flask import Blueprint, render_template, url_for, request, redirect
from .models import Professor, Class, Assignment, StatusLookup
from .extensions import db

main = Blueprint('main', __name__)


@main.route("/")
def index():
    professors = Professor.query.order_by(Professor.FullName.desc()).all()
    classes = Class.query.order_by(Class.Title.asc()).all()
    assignments = Assignment.query.order_by(Assignment.DueDate.asc()).all()
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

@main.route('/update_assignment/<int:AID>', methods=['GET', 'POST'])
def update_assignment(AID):
    assignment = Assignment.query.get_or_404(AID)
    classes = Class.query.all()
    status = StatusLookup.query.all()

    if request.method == 'POST':
        assignment.Title = request.form['title']
        assignment.Description = request.form['description']
        assignment.CID = request.form['class_name']
        assignment.DueDate = request.form['due_date']
        assignment.SID = request.form['status']
        assignment.Grade = request.form['grade']
        assignment.UpdatedDate = datetime.now()

        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('update_assignment.html', assignment=assignment, classes=classes, status=status)

@main.route('/update_class/<int:CID>', methods=['GET', 'POST'])
def update_class(CID):
    class_to_update = Class.query.get_or_404(CID)
    professors = Professor.query.all()

    if request.method == 'POST':
        class_to_update.Title = request.form['title']
        class_to_update.PID = request.form['professor_id']
        class_to_update.UpdatedDate = datetime.now()

        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('update_class.html', class_to_update=class_to_update, professors=professors)

@main.route('/update_professor/<int:PID>', methods=['GET', 'POST'])
def update_professor(PID):
    professor = Professor.query.get_or_404(PID)

    if request.method == 'POST':
        professor.FullName = request.form['full_name']
        professor.Email = request.form['email']
        professor.UpdatedDate = datetime.now()

        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('update_professor.html', professor=professor)

@main.route('/show_all_assignments')
def show_all_assignments():
    assignments = Assignment.query.order_by(Assignment.DueDate.asc()).all()
    return redirect(url_for('main.index'))


@main.route('/filter_assignment', methods=['GET', 'POST'])
def filter_assignment():

    query = Assignment.query

    if request.method == 'POST':
        class_id = request.form.get('class_name')
        status_id = request.form.get('status')

        if class_id:
            query = query.filter_by(CID=class_id)

        if status_id:
            query = query.filter_by(SID=status_id)

        assignments = query.order_by(Assignment.DueDate.asc()).all()

        return render_template(
            "index.html",
            assignments=assignments,
            classes=Class.query.all(),
            status=StatusLookup.query.all(),
            professors=Professor.query.all(),
            selected_class=class_id,
            selected_status=status_id
        )

    return render_template(
        "filter_assignment.html",
        classes=Class.query.all(),
        status=StatusLookup.query.all())

