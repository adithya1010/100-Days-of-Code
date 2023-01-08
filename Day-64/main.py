from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import sqlite3
from sqlalchemy import MetaData, Table, Column, Integer, String, Float

# Create a new database called movies-collection.db

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"
db = SQLAlchemy(app)
app.app_context().push()






# Create a new table

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(250))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Float)
    review = db.Column(db.String)
    img_url = db.Column(db.String)


#
db.create_all()

# new_movie = Movies(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# db.session.add(new_movie)
# db.session.commit()

movie_api_key = "598eef6bbf69401c173d3e79a40379dc"
movie_endpoint = "https://api.themoviedb.org/3/search/movie"


# Form for Rate Movie
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

# Form for Add Movie

class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    desc_movies = db.session.query(Movies).order_by(Movies.rating.desc()).all()
    for movie in desc_movies:
        movie.ranking = desc_movies.index(movie)+1
    db.session.commit()
    return render_template("index.html", movies=desc_movies)

@app.route("/edit")
def edit():
    # Getting the book id from parameter
    movie_id = request.args.get("id")
    # Getting the database column for the movie to be updated
    movie_to_update = Movies.query.get(movie_id)
    form = RateMovieForm()
    return render_template("edit.html", movie=movie_to_update, form=form)



@app.route("/delete")
def delete():
    # Getting the movie id from parameter
    movie_id = request.args.get("id")
    # Getting the column to be deleted from the database
    movie_to_delete = Movies.query.get(movie_id)
    # Deleting the chosen column
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        print(title)
        movie_parameters = {
            "api_key": movie_api_key,
            "query": title

        }
        movie_response = requests.get(movie_endpoint, movie_parameters)
        # print(movie_response.status_code)
        movie_data = movie_response.json()["results"]

        return render_template("select.html", options=movie_data)

    return render_template("add.html", form=form)


@app.route("/fetch")
def fetch():
    movie_id = request.args.get("id")
    # print(movie_id)
    movie_details_endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    movie_details_parameters = {
        "api_key" : movie_api_key,
    }
    movie_details_response = requests.get(movie_details_endpoint, movie_details_parameters)
    movie_details_data = movie_details_response.json()
    # print(movie_details_data)
    title = movie_details_data["title"]
    image_path = movie_details_data["poster_path"]
    images_url = f"https://image.tmdb.org/t/p/w500{image_path}"
    print(images_url)
    year = movie_details_data["release_date"]
    description = movie_details_data["overview"]
    new_movies = Movies(title=title, img_url=images_url, year=year, description=description)
    db.session.add(new_movies)
    db.session.commit()
    movie_to_update = Movies.query.get(movie_id)
    return redirect(url_for("edit_movie", id=new_movies.id))

@app.route("/edit", methods=["POST"])
def edit_movie():
    # Getting the movie id from the form
    form = RateMovieForm()
    movie_id = request.args.get("id")
    # Getting the column to be updated from the database
    movie_to_update = Movies.query.get(movie_id)
    # Changing the rating to the rating specified in the form
    movie_to_update.rating = float(form.rating.data)
    # Changing the rating to the rating specified in the form
    movie_to_update.review = form.review.data
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
