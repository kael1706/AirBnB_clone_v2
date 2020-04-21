#!/usr/bin/python3
"""Start a Flask web application"""


from flask import Flask


myapp = Flask(__name__)


@myapp.route('/', strict_slashes=False)
def home_render():
    """when url = /myhostname"""

    return "Hello HBNB!"


if __name__ == "__main__":
    myapp.run(host="0.0.0.0",
              port="5000")
