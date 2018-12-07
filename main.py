from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://vidauthc_usr:MakiCantik@104.250.105.85:3306/vidauthc_db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(50), nullable=False)
	phone_number = db.Column(db.String(20), nullable=False)
	otp_token = db.Column(db.String(16), nullable=False)
	is_confirmed = db.Column(db.Boolean, default=False)
	
	otp = db.relationship(
		'Otp', backref='user', lazy=True
		)
	otp = db.relationship(
		'Auth', backref='user', lazy=True, uselist=False
		)
	email_confirmation = db.relationship(
		'EmailConfirmation', backref='user', lazy=True
		)

class Otp(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	at = db.Column(db.DateTime, nullable=False)
	expire = db.Column(db.DateTime, nullable=False)

class UserAuth(db.Model):
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	tmd = db.Column(db.LargeBinary, nullable=True)
	face = db.Column(db.LargeBinary, nullable=True)
	voice = db.Column(db.LargeBinary, nullable=True)

class EmailConfirmation(db.Model):
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	token = db.Column(db.String(50), nullable=False)
	expire = db.Column(db.DateTime, nullable=False)

@app.route("/")
def hello():
    return "Hello World!"