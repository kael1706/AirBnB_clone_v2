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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """states"""
    s_l = storage.all(State)
    k = None
    state = None
    if id:
        k = 'State.{}'.format(id)
        if k in s_l.keys():
            state = s_l[k]

    return render_template(
        '9-states.html',
        id=k, state=state,
        states=s_l
    )


if __name__ == "__main__":
    app.run(
            host="0.0.0.0",
            port="5000")
