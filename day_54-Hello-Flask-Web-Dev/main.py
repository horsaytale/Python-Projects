# Noted to allow the Flask to run:-
# It's either you use local or command prompt
# if it's local, do it this way:-                    if it's command prompt, do it like normal
#           set FLASK_APP=main.py                           set FLASK_APP=main.py
#           $env:FLASK_APP = "main.py"                      flask run
#           flask run

from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrap_function():
        return f"<b>{function()}</b>"

    return wrap_function


def make_emphasis(function):
    def wrap_function():
        return f"<em>{function()}</em>"

    return wrap_function


def make_underlined(function):
    def wrap_function():
        return f"<u>{function()}</u>"

    return wrap_function


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center;'>Hello, World!</h1>" \
           "<p>This is my paragraph comment</p>" \
           "<img src='https://media.giphy.com/media/1wnZSnmrnwJmnJkd1c/giphy-downsized-large.gif' width=200>"


# The app is the object of the flask class as shown above
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"


@app.route("/username/<name>")  # @app.route("/<name>") another simpler method
def greet(name):
    return f"Hello there {name + '12'}!"


# @app.route("/username/<name>/1") you add more to the path if you want

@app.route("/<name>/<int:number>")
def awesome(name, number):
    return f"Yo yo {name}. I am {number} years old"


# @app.route("/<path:name>")
# def yoohooo(name):
#     return f"Hello there {name}!"

# Choose to activate the debugger
if __name__ == '__main__':
    app.run(debug=True)
