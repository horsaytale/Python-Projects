import os.path

from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap
import email_validator


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(allow_empty_local=True)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


app = Flask(__name__)

app.secret_key = '214sgae1412'
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    # Not necessary since can rely on built-in errors within the browser
    if login_form.validate_on_submit():  # This function is to allow the created errors shown in HTML to work
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
