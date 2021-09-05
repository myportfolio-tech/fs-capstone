import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    TESTING=True
