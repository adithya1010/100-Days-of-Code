import sqlite3
from flask import Flask

import sqlalchemy as db
from sqlalchemy import MetaData, Table, Column, Integer, String, Float
# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

engine = db.create_engine('sqlite:///new-books-collection.db', echo = True)
conn = engine.connect()
meta = MetaData()

students = Table(
   'books', meta,
   Column('id', Integer, primary_key = True),
   Column('title', String, nullable=False, unique=True),
   Column('author', String, nullable=False),
   Column('rating', Float, nullable=False)
)
meta.create_all(engine)


query = db.insert(students).values(id=1, title="Harry Potter", author="J.K.Rowling", rating=9.3)
Result = conn.execute(query)

output = conn.execute(students.select()).fetchall()
print(output)