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


@app.route('/states_list', strict_slashes=False)
def statesl_render():
    """render a list of states"""

    storage.reload()

    return render_template(
        '7-states_list.html',
        states=storage.all(State).values())


@app.route('/cities_by_states', strict_slashes=False)
def c_b_s_render():
    """cities by states"""

    storage.reload()

    return render_template(
        '8-cities_by_states.html',
        states=storage.all(State).values())


if __name__ == "__main__":
    app.run()
