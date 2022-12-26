from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

print(__name__)

random_no = random.randint(1, 10)

today = datetime.datetime.today()

year = today.year

print(year)
name="Adithya S.T."
@app.route('/')
def hello_world():
    return render_template("index.html", num = random_no, CURRENT_YEAR = year, YOUR_NAME = name )


@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", person_name=name, age=age, gender=gender)

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)