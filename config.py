import os

basedir=os.path.abspath(os.path.dirname(__name__))

class Config(object):
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'this-is-secret'
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
        'sqlite:///'+ os.path.join(basedir,'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False