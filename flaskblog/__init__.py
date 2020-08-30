from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
# secret key protects against modifying cookies and cross site request forgery attacks
app.config['SECRET_KEY'] = '49e6d85a0579ae61d87a0fea78dcade1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = flask_sqlalchemy
db = SQLAlchemy(app)

from flaskblog import routes