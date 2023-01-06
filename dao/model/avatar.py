from sqlalchemy import Column, Integer, String
from marshmallow import Schema, fields
from setup_db import base


class Avatar(base):
    __tablename__ = 'avatar'

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)


class AvatarSchema(Schema):
    id = fields.Int()
    url = fields.Str()
