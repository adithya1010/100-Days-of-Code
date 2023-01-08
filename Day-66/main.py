# Imports
import csv
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import sqlite3
from sqlalchemy import MetaData, Table, Column, Integer, String, Float
import requests
from flask import Flask, render_template, redirect, url_for, request
import requests
import pandas
import openpyxl

# Doing a GET Request

# response = requests.get("https://google.com")
# print(response.status_code)


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Initializing BootStrap for App
Bootstrap(app)
# Initializing database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///websites-collection.db"
db = SQLAlchemy(app)
app.app_context().push()


# Create a new table

class Websites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    status_code = db.Column(db.String)

# Create a New Form
class WebsiteForm(FlaskForm):
    website = StringField("Enter the website that you want to know the status of:")
    submit = SubmitField("Submit")


db.create_all()


# At home page render index.html as well as the form which asks the user to enter the table
@app.route("/")
def home():
    form = WebsiteForm()
    return render_template("index.html", form=form)


# When the user clicks on the submit button/makes a POST Request the webiste then checks whether the site is up or
# not using requests and checks the status code and depending on it the status site then reports whether the site is
# Up or Down
# The website and it's status are then stored in a database using SQLite and SQLAlchemy

@app.route("/", methods=["POST"])
def get_data():
    form = WebsiteForm()
    url = form.website.data
    print(url)
    try:
        response = requests.get(url)
        code = response.status_code
        print(code)
        site_status = "Up⬆️"
    except:
        site_status = "Down⬇️"
    new_website = Websites(name=url, status_code=site_status)
    db.session.add(new_website)
    db.session.commit()
    return render_template("status.html", status=site_status)


# In the check route the function for it gets the all the data present in the database as of now and passes it to the
# HTML file to be displayed on a table Also every url is checked everytime the site is refreshed/landed as each url
# is checked and then is updated in the SQL DB
@app.route("/check")
def check():
    websites = db.session.query(Websites).all()
    urls = db.session.query(Websites.name).all()
    ids = db.session.query(Websites.id).all()
    for id in ids:
    # print(urls)
        for url in urls:

            try:
                response = requests.get(url)
                code = response.status_code
                print(code)
                site_status_update = "Up"
            except:
                site_status_update = "Down"
            site_to_update = Websites.query.get(id)
            site_to_update.status_code = site_status_update
            db.session.commit()

    return render_template("check.html", websites=websites)

if __name__ == '__main__':
    app.run(debug=True)
