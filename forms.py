#this is the flask's form module where the customers can fill out a form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, SelectField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, InputRequired

class AddTaskForm(FlaskForm):
    str = TextAreaField('输入框', render_kw={"rows": 8, "placeholder": "在此放入文字"}, validators = [DataRequired()])
    submit = SubmitField("测试")

def passwordValidator(form, field):
    if field.data != '777777':
        raise ValidationError("密码不正确喔")

class SecretForm(FlaskForm):
    pathphrase = PasswordField('密码', render_kw={"placeholder": "输入密码"},validators = [passwordValidator])
    submit = SubmitField("输入")

class QueryForm(FlaskForm):
    #choices = [("user", "用户输入"), ("result", "统计数据")]
    choices = [("result", "统计数据")]
    fields = SelectField('Select Field', choices=choices, validators=[InputRequired()])
    submit = SubmitField("确定")