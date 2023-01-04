from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, TextAreaField, IntegerField, BooleanField,
                     RadioField, SelectField)
from wtforms.validators import InputRequired, Length, DataRequired, URL
from wtforms import validators
from flask import Flask
from flask_bootstrap import Bootstrap
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe location on Google Maps(URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g. 5:30 PM', validators=[DataRequired()])
    rating = SelectField('Coffee Rating', choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'],
                         validators=[DataRequired()])
    strength = SelectField('Wifi Strength Rating', choices=['❌','💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
                           validators=[DataRequired()])
    power_socket = SelectField('Power Socket Availability', choices=['❌', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'], validators=[DataRequired()])

    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open('cafe-data.csv', mode="a", newline='', encoding="utf8") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.cafe_location.data},"
                           f"{form.open_time.data},"
                           f"{form.close_time.data},"
                           f"{form.rating.data},"
                           f"{form.strength.data},"
                           f"{form.power_socket.data}")
        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
