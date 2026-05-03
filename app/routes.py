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
        
        status_id = request.form['status']
        grade = request.form.get('grade')

        if status_id == '3': 
            if not grade:
                raise ValueError("Grade required when status is Graded")
        else:
            grade = None 

        new_assignment = Assignment(
            Title=request.form['title'],
            Description=request.form['description'],
            CID=request.form['class_name'],
            DueDate=request.form['due_date'],
            SID=status_id,
            Grade=grade
        )
        try:
            db.session.add(new_assignment)

            db.session.commit()

            return redirect(url_for('main.index'))

        except:
            print("Adding assignment failed")

    return render_template('add_assignment.html', classes=classes, status=status)


@main.route('/add_class', methods=['GET', 'POST'])
def add_class():
    professors = Professor.query.all()

    if request.method == 'POST':
        new_class = Class(
            Title=request.form['title'],
            PID=request.form['professor_id']
        )
        try:
            db.session.add(new_class)
            db.session.commit()
            return redirect(url_for('main.index'))
        except:
            print("Adding class failed")
        
    

    return render_template('add_class.html', professors=professors)

@main.route('/add_professor', methods=['GET', 'POST'])
def add_professor():
    if request.method == 'POST':
        new_professor = Professor(
            FullName=request.form['full_name'],
            Email=request.form['email']
        )
        try:
            db.session.add(new_professor)
            db.session.commit()
            return redirect(url_for('main.index'))
        except:
            print("Adding professor failed")
       
        
    return render_template('add_professor.html')

@main.route('/delete_professor/<int:PID>')
def delete_professor(PID):
    professor = Professor.query.get_or_404(PID)
    try:
        db.session.delete(professor)
        db.session.commit()
    except:
        print("Deleting professor failed")
    return redirect('/')

@main.route('/delete_class/<int:CID>')
def delete_class(CID):
    class_todelete = Class.query.get_or_404(CID)
    try:
        db.session.delete(class_todelete)
        db.session.commit()
    except:
        print("Deleting class failed")
    return redirect('/')

@main.route('/delete_assignment/<int:AID>')
def delete_assignment(AID):
    assignment = Assignment.query.get_or_404(AID)
    try:
        db.session.delete(assignment)
        db.session.commit()
    except:
        print("Deleting assignment failed")
    return redirect('/')

@main.route('/update_assignment/<int:AID>', methods=['GET', 'POST'])
def update_assignment(AID):
    assignment = Assignment.query.get_or_404(AID)
    classes = Class.query.all()
    status = StatusLookup.query.all()

    if request.method == 'POST':
            status_id = request.form['status']
            grade = request.form.get('grade')

            if status_id == '3': 
                if not grade:
                    raise ValueError("Grade required when status is Graded")
            else:
                grade = None 

            new_assignment = Assignment(
                Title=request.form['title'],
                Description=request.form['description'],
                CID=request.form['class_name'],
                DueDate=request.form['due_date'],
                SID=status_id,
                Grade=grade
            )
            try:
                db.session.add(new_assignment)

                db.session.commit()

                return redirect(url_for('main.index'))

            except:
                print("Adding assignment failed")

    return render_template('update_assignment.html', assignment=assignment, classes=classes, status=status)

@main.route('/update_class/<int:CID>', methods=['GET', 'POST'])
def update_class(CID):
    class_to_update = Class.query.get_or_404(CID)
    professors = Professor.query.all()

    if request.method == 'POST':
        class_to_update.Title = request.form['title']
        class_to_update.PID = request.form['professor_id']
        class_to_update.UpdatedDate = datetime.now()
        try:
            db.session.commit()
            return redirect(url_for('main.index'))
        except:
            print("Updating class failed")

    return render_template('update_class.html', class_to_update=class_to_update, professors=professors)

@main.route('/update_professor/<int:PID>', methods=['GET', 'POST'])
def update_professor(PID):
    professor = Professor.query.get_or_404(PID)

    if request.method == 'POST':
        professor.FullName = request.form['full_name']
        professor.Email = request.form['email']
        professor.UpdatedDate = datetime.now()
        try:
            db.session.commit()
            return redirect(url_for('main.index'))
        except:
            print("Updating professor failed")
        

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

