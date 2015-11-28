__author__ = 'Sourabh Dev'

from flask import Flask, render_template, request, redirect, url_for
from flask import sessions, jsonify, flash

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item


app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Home Page for the application
@app.route('/')
def index():
    return render_template('index.html', categories=get_all_categories())


# Helper functions
def get_all_categories():
    categories = session.query(Category).order_by(asc(Category.name))
    return categories


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
