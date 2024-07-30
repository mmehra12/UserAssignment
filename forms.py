from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class AdminForm(FlaskForm):
    prefix = StringField('Username Prefix', validators=[DataRequired()])
    start = IntegerField('Start Range', validators=[DataRequired()])
    end = IntegerField('End Range', validators=[DataRequired()])
    submit = SubmitField('Generate Usernames')

class ParticipantForm(FlaskForm):
    workshop_username = StringField('Workshop Username', validators=[DataRequired()])
    submit = SubmitField('Get Username')

