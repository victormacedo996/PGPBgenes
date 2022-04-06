from flask import Blueprint, render_template
from datetime import datetime

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/en/home")
def home_en():
    date = datetime.now()
    return render_template('en/home_en.html', title='Home', date=date.year)

@main.route("/pt_br/home")
def home_pt_br():
    date = datetime.now()
    return render_template('pt_br/home_pt_br.html', title='Página inicial', date=date.year)


@main.route("/en/tutorials")
def tutorials_en():
   date = datetime.now()
   return render_template('en/tutorials_en.html', title='Tutorials', date=date.year)

@main.route("/pt_br/tutorials")
def tutorials_pt_br():
    date = datetime.now()
    return render_template('pt_br/tutorials_pt_br.html', title='Tutoriais', date=date.year)