from flask_wtf import FlaskForm  # Base class untuk semua form Flask-WTF
from wtforms import StringField, PasswordField, SubmitField  # Field yang digunakan di form
from wtforms.validators import DataRequired, Email, EqualTo, Length  # Validator input form

class RegisterForm(FlaskForm):  # Membuat form Register, turunan dari FlaskForm
    username = StringField("Username", validators = [
        DataRequired(),        # Wajib diisi
        Length(min = 3, max = 25)  # Minimal 3 karakter, maksimal 25
    ])
    
    email = StringField("Email", validators = [
        DataRequired(),
        Email()                # Harus format email valid
    ])
    
    password = PasswordField("Password", validators = [
        DataRequired(),
        Length(min = 6)          # Password minimal 6 karakter
    ])
    
    confirm = PasswordField("Confirm Password", validators = [
        EqualTo('password')    # Harus sama dengan field password
    ])
    
    submit = SubmitField("Register")  # Tombol submit
