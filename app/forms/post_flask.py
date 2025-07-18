# post_form.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField("Title", validators = [
        DataRequired()
        ])
    
    body = TextAreaField("Body", validators = [
        DataRequired()
        ])
    
    submit = SubmitField("Create Post")
