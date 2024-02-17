from flask import Flask, url_for, request
import os

app = Flask(__name__)


@app.route('/form_sample_get', methods=['POST', 'GET'])
def form_sample_get():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <center><h1>Анкета предендента</h1></center>
                            <center><h2>на участие в миссии</h2></center>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="text" placeholder="Введите фамилию" name="text">
                                    <input type="text" class="form-control" id="text" placeholder="Введите Имя" name="text">
                                    <h2><br></h2>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <h6><br></h6>
                                        <label for="about">Какие у вас есть профессии!</label>
                                        <p><input type="checkbox" name="a"> инженер-исследователь</p>
                                        <p><input type="checkbox" name="a"> пилот</p>
                                        <p><input type="checkbox" name="a"> строитель</p>
                                        <p><input type="checkbox" name="a"> экзобиолог</p>
                                        <p><input type="checkbox" name="a"> врач</p>
                                        <p><input type="checkbox" name="a"> инженер по терраформированию</p>
                                        <p><input type="checkbox" name="a"> климатолог</p>
                                        <p><input type="checkbox" name="a"> специалист по радиационной защите</p>
                                        <p><input type="checkbox" name="a"> астрогеолог</p>
                                        <p><input type="checkbox" name="a"> гляциолог</p>
                                        <p><input type="checkbox" name="a"> инженер жизнеобеспечения</p>
                                        <p><input type="checkbox" name="a"> метеоролог</p>
                                        <p><input type="checkbox" name="a"> оператор марсохода</p>
                                        <p><input type="checkbox" name="a"> киберинженер</p>
                                        <p><input type="checkbox" name="a"> штурман</p>
                                        <p><input type="checkbox" name="a"> пилот дронов</p>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <h6><br></h6>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
