'''Import Flask '''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

'''Instantiate a flask object'''
app = Flask(__name__,instance_relative_config=True)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

csrf = CSRFProtect(app)

from pkg import mymodels
from pkg.myroute import admin_route,user_routes

'''On the terminal, activate virtual environment, then python shell'''
from pkg import db