from data.users import User
from flask import Flask
from data import db_session
from data.jobs import Jobs

db_session.global_init("db/mars_explorer.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.hashed_password = '1111'
user.set_password(user.hashed_password)
user.email = "scott_chief@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Artem"
user.name = "Maikov"
user.age = 20
user.position = "bothman"
user.speciality = "teacher"
user.address = "nose"
user.hashed_password = '1111'
user.set_password(user.hashed_password)
user.email = "artem123@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Vasya"
user.name = "Nikonorof"
user.age = 22
user.position = "cook"
user.speciality = "boatswain"
user.address = "tail"
user.hashed_password = '1111'
user.set_password(user.hashed_password)
user.email = "vasya123@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Firsov"
user.name = "Dmitry"
user.age = 23
user.position = "pilot"
user.speciality = "flyer"
user.address = "tail"
user.hashed_password = '1111'
user.set_password(user.hashed_password)
user.email = "flyer332@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()