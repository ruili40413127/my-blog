# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

# 登陆表


class LoginForm(FlaskForm):
    email = StringField(label=u'email', validators=[
                        DataRequired(), Length(1, 64), Email()], id='loginlength')
    password = PasswordField(label=u'password', validators=[
                             DataRequired()], id='loginlength')
    remember_me = BooleanField(label=u'remember me', id='loginlength')
    submit = SubmitField(label=u'login')

# 注册表


class RegisterForm(FlaskForm):
    email = StringField(label=u'email address', validators=[
                        DataRequired(), Length(1, 64), Email()], id='registerlength')
    username = StringField(label=u'username', validators=[DataRequired(), Length(1, 64)],
                           id='registerlength')
    password = PasswordField(label=u'password', validators=[DataRequired(),
                                                      EqualTo('password2', message=u'The password must be the same')], id='registerlength')
    password2 = PasswordField(label=u'confirm you password', validators=[DataRequired(),
                                                      EqualTo('password', message=u'The password must be the same')], id='registerlength')
    submit = SubmitField(label=u'register now')
