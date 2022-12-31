from flask import Flask, render_template, request
import random
import datetime
import requests
import smtplib

app = Flask(__name__)

print(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

MY_EMAIL = "adithya.mailbot@gmail.com"
PASSWORD = "bashpyjrfaocrkdu"

@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html", msg_sent=False)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact", methods=["POST"])
def receive_data():
    name = request.form["username"]
    print(name)
    email = request.form["email"]
    print(email)
    phone = request.form["phone"]
    print(phone)
    message = request.form["message"]
    print(message)
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=MY_EMAIL, password=PASSWORD)  # Logging in using username and password
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:New Message\n\nName:{name}\nEmail:{email}\nPhone No:{phone}\nMessage:{message}"
        )  # sending mail with from
    # address, to address and message
    return render_template("contact.html", msg_sent=True)


if __name__ == "__main__":
    app.run(debug=True)