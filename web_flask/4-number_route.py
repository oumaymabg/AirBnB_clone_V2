#!/usr/bin/python3
"""
from flask import Flask
"""class Flask"""


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays "Hello HBNB!"
    Returns:
        Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """displays "HBNB"
    Returns:
        "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """display_C
    Args:
       display_C (str): display_C
    Returns:
       display_C
    """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """display_python
    Args:
       display_python (str): display_python
    Returns:
        display_python
    """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_num(n):
    """displays text
    Args:
        n (int): number
    Returns:
        string
    """
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)