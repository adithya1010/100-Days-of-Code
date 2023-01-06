from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from sqlalchemy import MetaData, Table, Column, Integer, String, Float

all_books = []


# Create a new database called books-collection.db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
db = SQLAlchemy(app)
app.app_context().push()


# Creating a new table

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET"])
def add():
    return render_template("add.html")


@app.route("/add", methods=["POST"])
def receive_data():
    # Getting the necessary inputs from the form and storing it in variables
    book_name = request.form["bookname"]
    print(book_name)
    author_name = request.form["author"]
    print(author_name)
    book_rating = request.form["rating"]
    print(book_rating)
    # Storing the variables in a dictionary
    # new_book = {
    #     "title": book_name,
    #     "author": author_name,
    #     "rating": book_rating
    # }
    new_book = Book(title=book_name, author=author_name, rating=book_rating)
    db.session.add(new_book)
    db.session.commit()
    # # Appending the dictionary into list creating list of dictionary
    # all_books.append(new_book)
    return redirect(url_for('home'))

@app.route("/edit")
def edit():
    # Getting the book id from parameter
    book_id = request.args.get("id")
    # Getting the database column for the book to be updated
    book_to_update = Book.query.get(book_id)
    return render_template("edit.html", book=book_to_update)

@app.route("/edit", methods=["POST"])
def edit_rating():
    # Getting the book id from the form
    book_id = request.form["id"]
    # Getting the column to be updated from the database
    book_to_update = Book.query.get(book_id)
    # Changing the rating to the rating specified in the form
    book_to_update.rating = request.form["new_rating"]
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/delete")
def delete():
    # Getting the book id from parameter
    book_id = request.args.get("id")
    # Getting the column to be deleted from database
    book_to_delete = Book.query.get(book_id)
    # Deleting the chosen column
    db.session.delete(book_to_delete)
    # Committing the changes
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
