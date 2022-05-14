import base64
import hashlib
import hmac

import jwt

from application.config import BaseConfig

from application.dao import UserDAO
from application.schemas.user import UserSchema


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao
        self.salt = BaseConfig.PWD_HASH_SALT
        self.iterations = BaseConfig.PWD_HASH_ITERATIONS
        self.secret = BaseConfig.SECRET_KEY
        self.algo = BaseConfig.PWD_JWT_ALGO
        self.min_exp = BaseConfig.TOKEN_EXPIRE_MINUTES
        self.days_exp = BaseConfig.TOKEN_EXPIRE_DAYS

    def get_user(self, user_id: int):
        """
        Сервис получения данных о пользователе
        :param: user_id: ind - ID пользователя
        :return: объект запроса к БД с данными о пользователе
        """
        user = self.dao.get_one_by_id(user_id)
        return {"id": user.id,
                "email": user.email,
                "name": user.name,
                "surname": user.surname}

    def get_hash(self, password):
        """
        Функция преобразования пароля пользователя в хеш строку.
        :param password: str - пароль пользователя
        :return: hp: str - хешированный пароль
        """
        try:
            hp = hashlib.pbkdf2_hmac(hash_name='sha256',
                                     password=password.encode('utf-8'),
                                     salt=self.salt,
                                     iterations=self.iterations)

            hp = base64.b64encode(hp)
            return hp

        # Если ошибка, то печатаем исключение
        except UnicodeDecodeError as e:
            print(f'Ошибка преобразования данных: {e}')

    def decode_token(self, token):
        decoded_token = jwt.decode(token, self.secret, algorithms=[self.algo])
        return decoded_token

    def compare_passwords(self, original_pass, pass_to_compare):
        """
        Метод проверки подлинности паролей
        :param original_pass: оригинальный пароль, хранящийся в БД
        :param pass_to_compare: пароль, который будет сравниваться с оригинальным
        :return: True - если совпадают
        """
        if hmac.compare_digest(original_pass, self.get_hash(pass_to_compare)):
            return True

    def update_userdata(self, user_data):
        user = self.dao.data_update(user_data)
        # Не возвращаем ничего
        # return UserSchema().dump(user)

    def update_userpass(self, token, passwords):
        """
        Сервис обновления пароля пользователя.
        :param token: токен пользователя.
        :param passwords: пароли пользователя (старый и тот, на который нужно заменить)
        :return: обновленные данные в виде json.
        """
        # Получаем данные из токена с помощью декодера
        data = self.decode_token(token)
        # Получаем объект пользователя по полученному email из токена
        user = self.dao.get_one_by_email(email=data.get('email'))
        # Если ошибка, то возвращаем ошибку
        if not self.compare_passwords(original_pass=user.password, pass_to_compare=passwords.get("old_password")):
            return {"error": "Пароли не совпадают"}
        # Меняем в объекте пароль
        user.password = self.get_hash(passwords.get("new_password"))
        # Проталкиваем объект на обновление
        user = self.dao.password_update(user)

        return UserSchema().dump(user)



