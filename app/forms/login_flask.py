from flask_wtf import FlaskForm  # Base class form Flask
from wtforms import StringField, PasswordField, SubmitField  # Field yang dipakai
from wtforms.validators import DataRequired  # Validator agar wajib diisi

class LoginForm(FlaskForm):
    username = StringField("Username", validators = [
        DataRequired()  # Harus diisi
    ])
    
    password = PasswordField("Password", validators = [
        DataRequired()  # Harus diisi
    ])
    
    submit = SubmitField("Login")  # Tombol submit
