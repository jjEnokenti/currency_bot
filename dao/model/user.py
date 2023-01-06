from sqlalchemy import Column, String, Integer
from marshmallow import Schema, fields
from setup_db import base


class User(base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    id = Column(Integer, unique=True)
    username = Column(String)
    full_name = Column(String, default=None)
    first_name = Column(String, default=None)
    last_name = Column(String, default=None)
    url_address = Column(String)


class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    id = fields.Int()
    username = fields.Str()
    full_name = fields.Str(default=None)
    first_name = fields.Str(default=None)
    last_name = fields.Str(default=None)
    url_address = fields.Str()
