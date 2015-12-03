__author__ = 'dev'

from flask import session as login_session

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


# Connect to Database and create database session
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def create_user(login_session):
    new_user = User(name=login_session['username'], email=login_session['email'], picture=login_session['picture'])
    session.add(new_user)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def get_user_info(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def get_user_id(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def get_all_categories():
    categories = session.query(Category).order_by(asc(Category.name))
    return categories


def user_logged_in():
    if 'username' not in login_session:
        return False
    return True