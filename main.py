from flask import Flask
import datetime

from data import db_sessions
from data.users import User

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


if __name__ == '__main__':
    os.remove("db/blogs.db")
    db_sessions.global_init("db/blogs.db")
    db_sess = db_sessions.create_session()

    for i in range(1, 4):
        user = User()
        user.name = f"Пользователь {i}"
        user.about = f"биография пользователя {i}"
        user.email = f"email{i}@email.ru"
        db_sess.add(user)
        db_sess.commit()

    user = db_sess.query(User).filter(User.id == 1).first()
    print(user)
    user.name = "Измененное имя пользователя"
    user.created_date = datetime.datetime.now()
    db_sess.commit()

    #app.run()
