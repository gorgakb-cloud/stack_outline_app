from flask import Blueprint, render_template
from .models import Professor, Class, Assignment

main = Blueprint('main', __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    professors = Professor.query.all()
    classes = Class.query.all()
    assignments = Assignment.query.all()
    return render_template("index.html", professors=professors, classes=classes, assignments=assignments)
