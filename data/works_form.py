import sqlalchemy
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, BooleanField, IntegerField
from wtforms.validators import DataRequired
from wtforms.fields import EmailField


class WorkForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
    team_leader = IntegerField('ID руководителя', validators=[DataRequired()])

    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    work_size = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    collaboratos = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.now)

    end_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                 default=datetime.datetime.now)

    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    user = orm.relationship("User")