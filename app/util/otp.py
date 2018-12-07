import pyotp
import time
import requests
from app.util.db import User, Otp, UserSession
from app import db

SMS_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTU0NDE5ODkwMywiZXhwIjo0MTAyNDQ0ODAwLCJ1aWQiOjY1MjI0LCJyb2xlcyI6WyJST0xFX1VTRVIiXX0.wiqiGzMWy-9ShuvCNYN2wtGOHY6AApYPllOMAaJEuwk'
SEND_MESSAGE_ENDPOINT = 'https://smsgateway.me/api/v4/message/send'

def generate_otp(email):
	seconds = int(time.time())
	user = User.query.filter_by(email=email).first()

	if user is None:
		invalid_email = {
		'status' : 'error',
		'message' : 'invalid email'
		} 
		return invalid_email

	hotp = pyotp.HOTP(user.otp_token)

	new_otp = Otp(user_id=user.id, at=seconds)
	db.session.add(new_otp)
	db.session.commit()

	#sendOtp
	otp = hotp.at(seconds)
	payload = [{
		"phone_number" : user.phone_number,
		"message" : "Your OTP code is " + otp + ".",
		"device_id" : 106529
	}]

	print(payload)

	header = {
		'Authorization' : SMS_TOKEN,
		# 'Content-Type' : 'application/json'
	}

	print(header)

	r = requests.post(SEND_MESSAGE_ENDPOINT, json=payload, headers=header)

	print(r.content)

	return {
		'status' : 'OK',
		'phone_number' : user.phone_number
	}

def verify_otp(email, otp_number):
	user = User.query.filter_by(email=email).first()

	hotp = pyotp.HOTP(user.otp_token)
	otp = Otp.query.filter_by(user_id=user.id).order_by('-id').first()

	if str(hotp.at(otp.at)) == str(otp_number) and time.time() < (otp.at+300):
		return {
			'status' : 'OK'
		}
	return {
		'status' : 'error',
		'message' : 'otp mismatch'
	}