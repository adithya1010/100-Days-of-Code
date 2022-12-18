from flask import Flask
app = Flask(__name__)
import random

@app.route('/')
def hello():
    return '<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


random_no = random.randint(0, 9)

@app.route("/<int:number>")
def no_entered(number):
    if number < random_no:
        return '<h1 style="color:red">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    if number > random_no:
        return '<h1 style="color:purple">Too High, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    if number == random_no:
        return '<h1 style="color:green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'



if __name__ == "__main__":
    app.run(debug=True)

