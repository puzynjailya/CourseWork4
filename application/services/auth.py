import calendar
import datetime
import jwt

from application.dao import UserDAO
from application.services.user import UserService


class AuthService(UserService):
    def __init__(self, dao: UserDAO):
        super().__init__(dao)
        self.dao = dao

    def create(self, data):
        """
        Сервис добавления данных нового пользователя в БД
        :param data: данные
        :return: сущность для добавления
        """
        data['password'] = self.get_hash(data['password'])
        self.dao.create(data)
        return data

    def create_tokens(self, user_data: dict, is_refresh=False):
        """
        Метод создания токенов для пользователя, который прошёл валидацию
        :param user_data: данные пользователя
        :param is_refresh: Флаг для функционала проверки access_token или refresh_token, default = False
        :return: tokens: dict - словарь с токенами (access, refresh)
        """
        user = self.dao.get_one_by_email(email=user_data.get('email'))

        # Ниже код, который можно расскоментить, если поиск будет по id
        # user = self.dao.get_one_by_id(id=user_data.get('id'))

        if user is None:
            return {"error": "Ошибка в запросе. Проверьте запрашиваемый email "}, 401

        if not is_refresh:
            if not self.compare_passwords(original_pass=user.password,
                                          pass_to_compare=user_data.get('password')):
                return {"error": "Проверьте правильность ввода пароля"}, 401

        # Создаем данные, для формирования токена
        data = {"email": user_data.get('email'),
                "password": user_data.get('password'),
                "name": user_data.get('name'),
                "surname": user_data.get('surname')}

        exp_minutes = datetime.datetime.utcnow() + datetime.timedelta(minutes=self.min_exp)
        data['exp'] = calendar.timegm(exp_minutes.timetuple())
        access_token = jwt.encode(data, self.secret, algorithm=self.algo)

        exp_days = datetime.datetime.utcnow() + datetime.timedelta(days=self.days_exp)
        data['exp'] = calendar.timegm(exp_days.timetuple())
        refresh_token = jwt.encode(data, self.secret, algorithm=self.algo)

        return {"access_token": access_token, "refresh_token": refresh_token}

    def approve_token(self, refresh_token):
        """
        Функция проверяет refresh_token и если он проходит проверку, то возвращает обновленные токены
        :param refresh_token: заданный для проверки refresh_token
        :return: dict {access_token:str, refresh_token:str}
        """
        try:
            decoded_token = self.decode_token(refresh_token)

        except Exception as e:
            return {"error": f"Ошибка обработки данных {e}"}, 401

        return self.create_tokens(decoded_token, is_refresh=True)


