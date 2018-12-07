from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://vidauthc_usr:MakiCantik@104.250.105.85:3306/vidauthc_db'
db = SQLAlchemy(app)


db.create_all()