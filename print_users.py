from data.users import User
from flask import Flask
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
bd_name = input()

db_session.global_init(bd_name)

db_sess = db_session.create_session()

for user in db_sess.query(User).filter(User.address == 'module_1', User.position.notilike("%engineer%"),
                                       User.speciality.notilike("%engineer%")).all():
    print(user.id)