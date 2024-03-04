from data.users import User
from flask import Flask
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/mars_explorer.db")
user = User()
user.name = "Scott"
user.surname = "Ridley"
user.age = 21

user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.hashed_password = '1234'
user.setPassword(user.hashed_password)
user.email = "scott_chief@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.name = "Andrey"
user.surname = "Ridl"
user.age = 21
user.position = "pilot"
user.speciality = "little_research engineer"
user.address = "module_2"
user.hashed_password = '1234'
user.setPassword(user.hashed_password)
user.email = "andy@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.name = "Dima"
user.surname = "Ridlov"
user.age = 38
user.position = "Cook"
user.speciality = "little_research cook"
user.address = "module_3"
user.hashed_password = '1234'
user.setPassword(user.hashed_password)
user.email = "dimas@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.name = "Vasya"
user.surname = "Roblox"
user.age = 17
user.position = "doctor"
user.speciality = "little_research doctor"
user.address = "module_4"
user.hashed_password = '1234'
user.setPassword(user.hashed_password)
user.email = "vasyan@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()