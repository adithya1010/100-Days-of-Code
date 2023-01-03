from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length, DataRequired
from wtforms import validators
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "Hi Chellam!"
bootstrap = Bootstrap(app)

class LoginForm(FlaskForm):
    email = StringField(label='Email',
                        validators=[DataRequired(), validators.Length(min=6, max=80)])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template('denied.html')
    return render_template("login.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)