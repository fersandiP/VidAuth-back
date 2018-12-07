from functools import wraps

from flask import request, jsonify
from . import app

from app.util.otp import verify_otp, generate_otp

INVALID_TOKEN = {
    'status' : 'error',
    'code' : 403,
    'message' : 'invalid token'
}

def need_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.form['token'] is not None:
            if verify_user(request.form['token']):
                return f(*args, **kwargs)
        return jsonify(INVALID_TOKEN)
    return decorated_function

@app.route('/')                       
def hello_world():
    return "hello_world"

#Send otp to client phone
@app.route('/otp/send', methods=['POST'])
def send_otp():
    if request.form['email'] is not None:
        resp = generate_otp(request.form['email'])
        return jsonify(resp)
    return jsonify({"status" : "error"})


#verification otp
@app.route('/otp/verify', methods=['POST'])
def verify_otp():
    if request.form['email'] is not None and request.form['otp'] is not None:
        resp = verify_otp(request.form['email'], request.form['otp'])
        return resp
    return jsonify({"status" : "error"})
    
#send confirmation email
@app.route('/email/send', methods=['POST'])
@need_token
def send_email():
    pass

#Confirm email
@app.route('/email/confirm')
def confirm_email():
    pass