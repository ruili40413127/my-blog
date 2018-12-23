# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from flask_pagedown.fields import PageDownField
from ..models import Role



class PostForm(FlaskForm):
    title = StringField(label=u'Title of blog', validators=[
                        DataRequired()], id='titlecode')
    body = PageDownField(label=u'Blog content', validators=[DataRequired()])
    submit = SubmitField(label=u'Submit')


class CommentForm(FlaskForm):
    body = PageDownField(label=u'Publish comment', validators=[DataRequired()])
    submit = SubmitField(label=u'submit')


class EditProfileForm(FlaskForm):
    name = StringField(label=u'true name', validators=[Length(0, 64)])
    location = StringField(label=u'address', validators=[Length(0, 64)])
    about_me = TextAreaField(label=u'about me')
    submit = SubmitField(label=u'submit')


class EditProfileAdministratorForm(FlaskForm):
    email = StringField(label=u'email', validators=[
                        DataRequired(), Length(1, 64), Email()])
    username = StringField(label=u'username', validators=[
                           DataRequired(), Length(1, 64)])
    confirmed = BooleanField(label=u'confirm')
    role = SelectField(label=u'role', coerce=int)

    name = StringField(label=u'true name', validators=[Length(0, 64)])
    location = StringField(label=u'address', validators=[Length(0, 64)])
    about_me = TextAreaField(label=u'about me')
    submit = SubmitField(label=u'submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdministratorForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name)]
        self.user = user
