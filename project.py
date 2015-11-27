__author__ = 'Sourabh Dev'

from flask import Flask, render_template, request, redirect, url_for
from flask import sessions, jsonify, flash


app = Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
