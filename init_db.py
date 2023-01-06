from dao.model.user import User
from setup_db import db, base


base.metadata.create_all(db)
