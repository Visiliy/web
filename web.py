from flask import Flask, flash, url_for
from flask import render_template, redirect, request, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import json
from random import randint
import urllib.request
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static/img/'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.secret_key = "cairocoders-ednalan"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class LoginForm(FlaskForm):
    command1 = StringField('id астронавта', validators=[DataRequired()])
    command2 = PasswordField('Пароль астронавта', validators=[DataRequired()])
    command3 = StringField('id капитана', validators=[DataRequired()])
    command4 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/<tile>')
@app.route('/index/<tile>')
def index(tile):
    text = 'Миссия Колонизация Марса'
    diviz = 'И на Марсе будут яблони цвести!'
    return render_template('index.html', title=tile,
                           misia=text, diviz=diviz)


@app.route('/training/<prof>')
def training(prof):
    text = 'Миссия Колонизация Марса'
    diviz = 'И на Марсе будут яблони цвести!'
    return render_template('odd_even.html', title=prof,
                           misia=text, diviz=diviz, prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    text = 'Миссия Колонизация Марса'
    diviz = 'И на Марсе будут яблони цвести!'
    return render_template('list.html', title=list,
                           misia=text, diviz=diviz, list=list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    text = 'Миссия Колонизация Марса'
    diviz = 'И на Марсе будут яблони цвести!'
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/list_prof/ol')
    return render_template('login.html', title='Авторизация', form=form, diviz=diviz, misia=text)


@app.route('/table/<gender>/<age>')
def table(gender, age):
    age = int(age)
    text = 'Миссия Колонизация Марса'
    diviz = 'И на Марсе будут яблони цвести!'
    return render_template('table.html', title='Цвет каюты',
                           misia=text, diviz=diviz, gender=gender, age=age)


@app.route('/member')
def member():
    text = 'Миссия Колонизация Марса'
    diviz = 'И на Марсе будут яблони цвести!'
    with open("templates/news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
        sws = news_list['star'][randint(0, 3)]
        df = ", ".join(sorted(sws['prof']))
    return render_template('member.html', title='Личная карточка',
                           misia=text, diviz=diviz, sws=sws, df=df)


@app.route('/carousel')
def carousel():
    text = 'Миссия Колонизация Марса'
    diviz = 'И на Марсе будут яблони цвести!'
    title = 'Пейзажи Марса'
    return render_template('carousel.html')


@app.route('/distribution')
def distribution():
    text = 'Миссия Колонизация Марса'
    diviz = 'И на Марсе будут яблони цвести!'
    title = 'По каютам!'
    n = 'Каюта №'
    command = ['Ридли скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тенди Сандерс', 'Шон Бин']
    return render_template('distribution.html', misia=text,
                           diviz=diviz, title=title, n=n, command=command)


@app.route('/')
def home():
    return render_template('load_photo.html', filename='/static/img/MARS-6.png')


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    if request.method == 'GET':
        return render_template('load_photo.html', filename='/static/img/MARS-6.png')
    elif request.method == 'POST':
        file = request.files['file']
        print(file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filename = '/static/img/' + filename
        return render_template('load_photo.html', filename=filename)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
