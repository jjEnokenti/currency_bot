from sqlalchemy.orm import sessionmaker

from setup_db import db
from dao.user import UserDAO
from service.user import UserService


Session = sessionmaker(db)
session = Session()

user_dao = UserDAO(session)
user_service = UserService(user_dao)
