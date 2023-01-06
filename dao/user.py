from dao.model.user import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        users = self.session.query(User).all()

        return users

    def get_one_by_id(self, user_id):
        user = self.session.query(User).\
            filter(User.id == user_id).first()
        self.session.close()
        return user

    def create(self, data):
        with self.session.begin():
            user = User(**data)
            self.session.add(user)

        return user
