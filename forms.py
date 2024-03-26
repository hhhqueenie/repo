#this is the flask's form module where the customers can fill out a form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    str = StringField('输入框', validators = [DataRequired()])
    submit = SubmitField("测试")
