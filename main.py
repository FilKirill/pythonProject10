from flask import Flask, url_for, render_template, redirect, abort, request
from data.users import User
from flask import Flask
from data.login_form import LoginForm
from flask_login import LoginManager, login_manager, login_user, logout_user, login_required, current_user
from data import db_session
from data.jobs import Jobs
from data.registration import RegForm
from data import jobs_api
from flask_restful import reqparse, abort, Api, Resource
from data import users_resource

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

db_session.global_init('db/mars_explorer.db')

api.add_resource(users_resource.UsersListResource, '/api/v2/user')

# для одного объекта
api.add_resource(users_resource.UsersResource, '/api/v2/user/<int:user_id>')

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/jobs')
def jobs():
    db_sess = db_session.create_session()

    jobs = db_sess.query(Jobs).all()

    return render_template('jobs.html', jobs=jobs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/jobs")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/add_jobs', methods=['GET', 'POST'])
@login_required
def add_job():
    form = WorksForm()
    if form.validate_on_submit() and form.team_leader.data != current_user.id:
        return render_template('works.html', title='Добавление работы',
                               form=form, message='Вы можете добавлять работы только от своего имени.')

    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs()
        job.team_leader = form.team_leader.data
        job.job = form.job.data
        job.is_finished = form.is_finished.data
        job.collaborators = form.collaborators.data
        job.work_size = form.work_size.data
        db_sess.add(job)
        db_sess.commit()
        return redirect('/jobs')
    return render_template('works.html', title='Добавление работы',
                           form=form)


@app.route('/register', methods=['GET', 'POST'])
def registration():
    form = RegForm()
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    if form.validate_on_submit() and form.email.data in [user.email for user in users]:
        return render_template('registration.html', title='Зарегистрироваться',
                               form=form, message='Существующая почта')
    if form.validate_on_submit() and form.password.data != form.password_2.data:
        return render_template('registration.html', title='Зарегистрироваться',
                               form=form, message='Пароли не равны')

    if form.validate_on_submit() and not (28 < form.age.data < 100):
        return render_template('registration.html', title='Зарегистрироваться',
                               form=form, message='Извините, вы не подходите к нам по возрасту.')

    if form.validate_on_submit() and form.password.data == form.password_2.data:
        db_sess = db_session.create_session()
        user = User()
        user.surname = form.surname.data
        user.name = form.name.data
        user.age = form.age.data
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.address = form.address.data
        user.email = form.email.data
        user.hashed_password = form.password.data
        user.set_password(user.hashed_password)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')

    return render_template('registration.html', title='Зарегистрироваться',
                           form=form)


@app.route('/job/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_work(id):
    form = WorksForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        work = db_sess.query(Jobs).filter(Jobs.id == id,
                                          (Jobs.team_leader == current_user.id) | (current_user.id == 1)
                                          ).first()
        if work:
            form.team_leader.data = work.team_leader
            form.job.data = work.job
            form.work_size.data = work.work_size
            form.collaborators.data = work.collaborators
            form.is_finished.data = work.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        work = db_sess.query(Jobs).filter(Jobs.id == id,
                                          (Jobs.team_leader == current_user.id) | (current_user.id == 1)
                                          ).first()
        if work:
            work.team_leader = form.team_leader.data
            work.job = form.job.data
            work.work_size = form.work_size.data
            work.collaborators = form.collaborators.data
            work.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/jobs')
        else:
            abort(404)
    return render_template('work_edit.html',
                           title='Редактирование работы',
                           form=form
                           )


@app.route('/job_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == id,
                                     (Jobs.team_leader == current_user.id) | (current_user.id == 1)
                                     ).first()
    if job:
        db_sess.delete(job)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/jobs')


if __name__ == '__main__':
    app.register_blueprint(jobs_api.blueprint)
    app.run(port=5050, host='127.0.0.1')