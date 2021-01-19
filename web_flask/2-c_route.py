#!/usr/bin/python3
"""task2: start a flask web application"""
from flask import Flask
"""classes Flask and import flask """
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays "Hello HBNB!"
    Returns:
        "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """displays hbnb
    Returns:
        hbnb
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """displays text
    Args:
        text (str): text
    Returns:
        text
    """
    return 'C %s' % text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
