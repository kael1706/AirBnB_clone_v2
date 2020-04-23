#!/usr/bin/python3
"""Starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """teardown storage"""

    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters_action(id=None):
    """hbnb filters"""

    return render_template(
        '10-hbnb_filters.html',
        states=storage.all(State).values(),
        amenities=storage.all(Amenity).values()
    )


if __name__ == "__main__":
    app.run(
            host="0.0.0.0",
            port="5000")
