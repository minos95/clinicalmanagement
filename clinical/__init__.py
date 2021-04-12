from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app= Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinical.db'
app.config['SECRET_KEY']='370fea70834bba1468d28654'
db = SQLAlchemy(app)
login_manager=LoginManager(app)
login_manager.login_view="index"
from clinical import routes
 