from sqlalchemy import ForeignKey, Column, String, Integer, BIGINT
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields

from dao.model.avatar import AvatarSchema
from dao.model.picture import PictureSchema
from setup_db import base


class User(base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    id = Column(BIGINT, unique=True)
    username = Column(String)
    full_name = Column(String, default=None)
    first_name = Column(String, default=None)
    last_name = Column(String, default=None)
    url_address = Column(String)
    avatar_id = Column(Integer, ForeignKey("avatar.id"))

    avatar = relationship("Avatar")
    picture = relationship("Picture")


class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    id = fields.Int()
    username = fields.Str()
    full_name = fields.Str(default=None)
    first_name = fields.Str(default=None)
    last_name = fields.Str(default=None)
    url_address = fields.Str()
    avatar_id = fields.Int()

    avatar = fields.Nested(AvatarSchema)
    picture = fields.Nested(PictureSchema)
