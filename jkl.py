import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/img/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/load_photo', methods=['GET', 'POST'])
def upload_file():
    file_static = 'MARS-6.png'
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('ERROR')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('ERROR')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_static = filename
            return render_template('load_photo.html', file_name=f'/static/img/{filename}')
    return render_template('load_photo.html', file_name=f'/static/img/{file_static}')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
