#!/usr/bin/python3
from flask import Flask
from flask import render_template
"""import class Flask,  Number template method"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays hello_hbnb
    Returns:
       hello_hbnb
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
      display_C(str): display_C
    Returns:
       display_C
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
    """displays HTML
    Args:
        n (int): number
    Returns:
        HTML page
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
