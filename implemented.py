from sqlalchemy.orm import sessionmaker

from setup_db import db
from dao.user import UserDAO
from service.user import UserService


Session = sessionmaker(db)

user_dao = UserDAO(Session())
user_service = UserService(user_dao)
