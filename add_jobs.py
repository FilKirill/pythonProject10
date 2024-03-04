from data.users import User
from flask import Flask
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/mars_explorer.db")
job = Jobs()
job.team_leader = 3
job.job = 'Посадить деревья'
job.work_size = 10
job.collaborators = '1, 2, 3'
job.is_finished = False
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()


job = Jobs()
job.team_leader = 3
job.job = 'Посадить кусты'
job.work_size = 10
job.collaborators = '1, 2'
job.is_finished = False
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()

job = Jobs()
job.team_leader = 3
job.job = 'Заделать забор'
job.work_size = 23
job.collaborators = '1'
job.is_finished = True
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()