#!/usr/bin/python3
""" task3 :starts a Flask web application"""
from flask import Flask
"""class Flask"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays hello hbnb
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


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """displays  c
    Args:
        display c  (str): display c
    Returns:
        display c
    """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """displays python
    Args:
        python (str): python
    Returns:
        python
    """
    return 'Python %s' % text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
@app.route('/number/<int:n>', strict_slashes=False)
def display_num(n):
    """displays text
    Args:
        n (int): number
    Returns:
        string
    """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_HTML(n):
    """displays text
    Args:
        n (int): number
    Returns:
        HTML page
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_odd_even(n):
    """displays text
    Args:
        n (int): number
    Returns:
        HTML page
    """
    if n % 2 == 0:
        desc = 'even'
    else:
        desc = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, desc=desc)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
