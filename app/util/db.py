from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(50), nullable=False)
	phone_number = db.Column(db.String(20), nullable=False, unique=True)
	otp_token = db.Column(db.String(16), nullable=False)
	is_confirmed = db.Column(db.Boolean, default=False)
	
	otp = db.relationship(
		'Otp', backref='user', lazy=True
		)
	email_confirmation = db.relationship(
		'EmailConfirmation', backref='user', lazy=True
		)
	user_session = db.relationship(
		'UserSession', backref='user', lazy=True
		)

class Otp(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	at = db.Column(db.Integer, nullable=False)

class UserAuth(db.Model):
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	tmd = db.Column(db.LargeBinary, nullable=True)
	face = db.Column(db.LargeBinary, nullable=True)
	voice = db.Column(db.LargeBinary, nullable=True)

class EmailConfirmation(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	token = db.Column(db.String(50), nullable=False)
	expire = db.Column(db.Integer, nullable=False)

class UserSession(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def dummy_data():
	user = User(email='fersandi19.91@gmail.com', phone_number='+6281367173222', otp_token='I7V5XE2IWIFPXEIB', is_confirmed=False)
	db.session.add(user)
	db.session.commit()