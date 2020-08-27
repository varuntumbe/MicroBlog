from flask import Flask,render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app=Flask(__name__)
app.config.from_object(Config)

#creating database instance
db = SQLAlchemy(app)

#creating migration instance
migrate=Migrate(app,db)

#creating Loginmanager instance
login=LoginManager(app)
login.login_view='login'

from app import routes,models,errors