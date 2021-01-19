#!/usr/bin/python3
""" Start a flask web application"""
from flask import flask
""" import flask """
app = flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display "Hello HBNB!"
    return "Hello HBNB" """

return “Hello HBNB!”
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
