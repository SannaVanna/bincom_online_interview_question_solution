from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import routes
from .db import db

app = Flask(__name__, static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_bincom_test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)



app.secret_key = "mybinconinterviewtesquestionsolution"
app.config['DEBUG'] = True
app.register_blueprint(routes, url_prefix="/")
