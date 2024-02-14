from flask import Flask
from flask import render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
