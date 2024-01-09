#!/usr/bin/env python3
"""initialize the flask app
"""
from flask import Flask, render_templates

app = Flask(__name__)


@app.route('/')
def index():
    """ render the index templates """
    return render_templates('index.html')


if __name__ == '__main__':
    app.run(debug=True)
