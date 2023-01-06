from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields

# from dao.model.user import UserSchema
from setup_db import base


class Picture(base):
    __tablename__ = 'picture'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    url = Column(String, nullable=False)

    # user = relationship("User")


class PictureSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    url = fields.Str()

    # user = fields.Nested(UserSchema)
