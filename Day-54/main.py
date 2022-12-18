from flask import Flask

app = Flask(__name__)

print(__name__)


# Declaring decorators for making text bold,italic and underlined
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, there World!</h1>' \
           '<p> This is a paragraph</p>'\
           '<img src ="https://media.tenor.com/bK1qpWGyQKkAAAAM/kitty.gif">'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}! you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
