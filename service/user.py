from dao.user import UserDAO


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one_by_id(self, user_id):
        return self.dao.get_one_by_id(user_id)

    def create(self, data):
        return self.dao.create(data)
