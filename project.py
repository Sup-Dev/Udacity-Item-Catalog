__author__ = 'Sourabh Dev'

from flask import Flask, render_template, request, redirect, url_for
from flask import sessions, jsonify, flash


app = Flask(__name__)


# Home Page for the application
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
