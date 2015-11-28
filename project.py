__author__ = 'Sourabh Dev'

from flask import Flask, render_template, request, redirect, url_for
from flask import sessions, jsonify, flash

from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

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
    items = session.query(Item).order_by(desc(Item.created_date))
    return render_template('index.html', categories=get_all_categories(), items=items)


# Page shows items in a category
@app.route('/<category>/items')
def category_items(category):
    try:
        category = session.query(Category).filter_by(name=category).one()
        items = session.query(Item).filter_by(category=category)
        return render_template('category_items.html', categories=get_all_categories(), items=items)
    except NoResultFound:
        return redirect(url_for('index'))


# Helper functions
def get_all_categories():
    categories = session.query(Category).order_by(asc(Category.name))
    return categories


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
