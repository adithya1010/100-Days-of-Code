from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import random
from sqlalchemy import func

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# app.app_context().push()


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


# db.create_all()

@app.route("/")
def home():
    return render_template("index.html")


# Random route

@app.route("/random", methods=["GET"])
def get_random_cafe():
    # Getting the number of rows present in the database
    your_query = """
    SELECT count(*) from table
    """
    # no_of_rows = db.session.query(func.count(Cafe.id)).scalar()
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(
        # jsonify the cafe data
        id=random_cafe.id,
        name=random_cafe.name,
        map_url=random_cafe.map_url,
        img_url=random_cafe.img_url,
        location=random_cafe.location,
        seats=random_cafe.seats,
        has_toilet=random_cafe.has_toilet,
        has_wifi=random_cafe.has_wifi,
        has_sockets=random_cafe.has_sockets,
        can_take_calls=random_cafe.can_take_calls,
        coffee_price=random_cafe.coffee_price
    )

# Get All Cafes
@app.route('/all')
def all():
    cafes_list = []
    cafes = db.session.query(Cafe).all()
    for cafe in cafes:
        individual_cafe = {
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        }
        cafes_list.append(individual_cafe)
    return jsonify(cafes_list)


## HTTP GET - Read Record


@app.route('/search')
def search():
    # Getting the loc parameter

    loc = request.args.get("loc")

    try:
        cafe_search = Cafe.query.filter_by(location=loc).first()
        return jsonify(
            # jsonify the cafe data
            id=cafe_search.id,
            name=cafe_search.name,
            map_url=cafe_search.map_url,
            img_url=cafe_search.img_url,
            location=cafe_search.location,
            seats=cafe_search.seats,
            has_toilet=cafe_search.has_toilet,
            has_wifi=cafe_search.has_wifi,
            has_sockets=cafe_search.has_sockets,
            can_take_calls=cafe_search.can_take_calls,
            coffee_price=cafe_search.coffee_price
        )
    except:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"})


## HTTP POST - Create Record

# add test

@app.route('/add', methods=["POST"])
def add():
    form_data = request.form.to_dict()
    for key, value in form_data.items():
        if value.title() == "True":
            form_data[key] = True
        elif value.title() == "False":
            form_data[key] = False
    cafe = Cafe(**form_data)
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["GET", "PATCH", "POST"])
def update_a_cafe(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})





## HTTP DELETE - Delete Record

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_a_cafe(cafe_id):
    api_key = request.args.get("api-key")
    cafe = db.session.query(Cafe).get(cafe_id)
    if api_key == "TopSecretAPIKey":
        try:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."})
        except:
            return jsonify(response={"error": "Sorry a cafe with that id was not found in the database"})

    else:
        return jsonify(response={"error": "Sorry, that's not allowed. Make sure you have the correct API Key"})

if __name__ == '__main__':
    app.run(debug=True)
