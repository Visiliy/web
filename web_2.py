import sqlite3

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    connection = sqlite3.connect('db/citi_table.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    username TEXT NOT NULL,
    citi_name TEXT NOT NULL,
    citi_photo TEXT NOT NULL
    )
    ''')
    cursor.execute('INSERT INTO Users (name, username, citi_name, citi_photo) VALUES (?, ?, ?, ?)', (
        'Mark', 'Watny', 'Hometown Moscow',
        'https://static-maps.yandex.ru/1.x/?ll=37.646930,55.725146&spn=0.02,0.02&l=sat'))
    cursor.execute('INSERT INTO Users (name, username, citi_name, citi_photo) VALUES (?, ?, ?, ?)', (
        'Andy', 'Weir', 'Hometown Wellington',
        'https://static-maps.yandex.ru/1.x/?ll=174.781448,-41.290000&spn=0.02,0.02&l=sat'))
    connection.commit()
    connection.close()


@app.route('/users_show/<int:user_id>')
def users_show(user_id):
    return '<h1>Ok</h>'


if __name__ == '__main__':
    main()
    app.run(port=5000, host='127.0.0.1')
