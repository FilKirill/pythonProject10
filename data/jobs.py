import datetime
import sqlalchemy
from flask import redirect, render_template
from flask_login import login_user

from . import db_session
from .db_session import SqlAlchemyBase
from sqlalchemy import orm

from .login_form import LoginForm
from .users import User


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    team_leader = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))

    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    work_size = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    collaboratos = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.now)

    end_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                 default=datetime.datetime.now)

    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    user = orm.relationship("User")