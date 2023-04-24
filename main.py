from flask import Flask, render_template, redirect, request
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('register.html')


@app.route('/casino')
def casino():
    return render_template('casino.html')


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=8000, host='127.0.0.1', debug=True)