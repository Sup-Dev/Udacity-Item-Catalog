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
@app.route('/catalog/<category>/items')
def category_items(category):
    try:
        category_item = session.query(Category).filter_by(name=category).one()
        items = session.query(Item).filter_by(category=category_item)
        return render_template('category_items.html', categories=get_all_categories(), items=items, curr_cat=category)
    except NoResultFound:
        return redirect(url_for('index'))


# Gives description of the given item
@app.route('/catalog/<category>/<item>')
def item_description(category, item):
    try:
        category_item = session.query(Category).filter_by(name=category).one()
        item_content = session.query(Item).filter_by(category=category_item, title=item).one()
        return render_template('item_description.html', item=item, description=item_content.description)
    except NoResultFound:
        return redirect(url_for('index'))


# Add menu item
@app.route('/catalog/new', methods=['GET', 'POST'])
def item_new():
    try:
        if request.method == 'POST':
            category = session.query(Category).filter_by(name=request.form['category']).one()
            item = Item(title=request.form['title'], description=request.form['description'], category=category)
            session.add(item)
            return redirect(url_for('index'))
        else:
            categories = session.query(Category).all()
            return render_template('item_add.html', categories=categories)
    except NoResultFound:
        return redirect(url_for('index'))


# Edit menu item
@app.route('/catalog/<item_id>/edit', methods=['GET', 'POST'])
def item_edit(item_id):
    try:
        item = session.query(Item).filter_by(id=item_id).one()
        if request.method == 'POST':
            #flash("Item Edited")
            item.title = request.form['title']
            item.description = request.form['description']
            item_category = session.query(Category).filter_by(name=request.form['category']).one()
            item.category = item_category
            session.commit()
            return redirect(url_for('index'))
        else:
            categories = session.query(Category).all()
            return render_template('item_edit.html', item=item, categories=categories)
    except NoResultFound:
        return redirect(url_for('index'))


# Delete menu item
@app.route('/catalog/<item_id>/delete', methods=['GET', 'POST'])
def item_delete(item_id):
    try:
        item = session.query(Item).filter_by(id=item_id).one()
        if request.method == 'POST':
            #flash("Item Deleted")
            session.delete(item)
            session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('item_delete.html', item=item)
    except NoResultFound:
        return redirect(url_for('index'))


# Helper functions
def get_all_categories():
    categories = session.query(Category).order_by(asc(Category.name))
    return categories


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
