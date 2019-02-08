from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask

app = Flask(__name__)


db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

user_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True, strict=True)