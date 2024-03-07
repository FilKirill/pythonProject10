import datetime
from data.users import User
from flask import Flask
from data import db_session
from data.jobs import Jobs

db_session.global_init("db/mars_explorer.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

job = Jobs()
job.team_leader = 1
job.job = "deployment of residential modules 1 and 2"
job.work_size = 15
job.collaborators = " 2, 3"
job.is_finished = False
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()

job = Jobs()
job.team_leader = 1
job.job = 'Посадить деревья'
job.work_size = 10
job.collaborators = '1, 2, 3'
job.is_finished = False
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()

job = Jobs()
job.team_leader = 1
job.job = 'Покрасить забор завтра'
job.work_size = 5
job.collaborators = '1, 2, 3'
job.is_finished = True
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()


job = Jobs()
job.team_leader = 1
job.job = 'Вытащить васю в качалку'
job.work_size = 10
job.collaborators = '1'
job.is_finished = False
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()