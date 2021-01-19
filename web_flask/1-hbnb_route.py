#!/usr/bin/python3
""" task1: Start a flask web application"""
from flask import flask
""" import flask """
app = flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays hello hbnb!
    Returns:
        hello hbnb
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """displays hbnb
    Returns:
        hbnb
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
