from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lsvmfmhfakqeww:4487f7c99f8f91668e512f2355980d0303963c973c360e65dd1a88a315c94d3d@ec2-54-197-234-33.compute-1.amazonaws.com:5432/d1b2ko703609oh'
db = SQLAlchemy(app)

from app.util.db import *

from app.main import *

# db.create_all()
# dummy_data()