from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class WorksForm(FlaskForm):
    team_leader = IntegerField('id лидера', validators=[DataRequired()])
    job = StringField('Название работы', validators=[DataRequired()])
    work_size = IntegerField('Время работы', validators=[DataRequired()])
    collaborators = StringField('Участники работы', validators=[DataRequired()])
    is_finished = BooleanField("Закончено ли ?")
    submit = SubmitField('Применить')
