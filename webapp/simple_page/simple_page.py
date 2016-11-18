from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from webapp.simple_page import database

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/list', methods=['GET'])
def show():
    print (database.list_quizz)
    try:
        return render_template('quizz/list-quizz.html', les_quizzes = database.list_quizz)
    except TemplateNotFound:
        abort(404)

@simple_page.route('/create-quizz')
def create_quizz():
    try:
        return render_template('quizz/create-quizz.html')
    except TemplateNotFound:
        abort(404)

@simple_page.route('/')
def index():
    try:
        return render_template('quizz/index.html')
    except TemplateNotFound:
        abort(404)

@simple_page.route('/playquizz')
def playquizz():
    try:
        return render_template('quizz/play-quizz.html', traductions = database.traductions)
    except TemplateNotFound:
        abort(404)


@simple_page.route('/save')
def save():
    print("ca marche")
    try:
        return render_template('quizz/save.html')
    except TemplateNotFound:
        abort(404)

@simple_page.route('/test')
def test():
    eleves = range(1001)
    try:
        return render_template('quizz/test.html', ma_liste=eleves)
    except TemplateNotFound:
        abort(404)

@simple_page.route('/sauver', methods=['POST'])
def hello():
    print(database.list_quizz)
    database.list_quizz.append("David")
    print(database.list_quizz)

    return ""
    #name=request.form['yourname']
    #email=request.form['youremail']
    #return render_template('form_action.html', name=name, email=email)



