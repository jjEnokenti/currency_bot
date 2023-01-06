import json

from config import Config
from implemented import user_service
from dao.model.user import UserSchema


class DataHandler:
    def get_data(self):
        with open(Config.DATA_JSON, encoding="utf-8") as file:
            return json.load(file)

    def log_message(self, message):
        is_exist = user_service.get_one_by_id(message.from_user.id)
        if not is_exist:
            result = f"user id: {message.from_user.id}\n" \
                     f"username: {message.from_user.username}\n" \
                     f"first name: {message.from_user.first_name}\n" \
                     f"last name: {message.from_user.last_name}\n" \
                     f"full name: {message.from_user.full_name}\n" \
                     f"url: {message.from_user.url}\n" \
                     f"Message: {message.text}"
        else:
            result = f"user id: {is_exist.id}\n" \
                     f"username: {is_exist.username}\n" \
                     f"first name: {is_exist.first_name}\n" \
                     f"last name: {is_exist.last_name}\n" \
                     f"full name: {is_exist.full_name}\n" \
                     f"url: {is_exist.url_address}\n" \
                     f"Message: {message.text}"

        return result

    def form_answer(self):
        data = self.get_data()
        answer = []

        for cur in data:
            answer.append(f"{cur.get('count')} {cur.get('currency')} = "
                          f"{round(float(cur.get('price')), 3)} RUB")

        return answer

    def form_data(self, data):
        url = data.from_user.url
        data["from"]["url_address"] = url
        return UserSchema().dump(data["from"])
