#!/usr/bin/python3
"""Start a Flask web application"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home_render():
    """when URL = / """

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_render():
    """when URL = /hbnb"""

    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_render(text):
    """when URL = /<text>"""

    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_render(text='is cool'):
    """when URL = /python or /python<text>"""

    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_render(n):
    """number_render"""

    if isinstance(n, int):
        return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port="5000")
