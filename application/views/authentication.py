from flask import request, abort
from flask_restx import Resource, Namespace
from marshmallow.exceptions import MarshmallowError

from application.implemented import auth_service
from application.schemas.user import UserSchema

auth_ns = Namespace('auths')


@auth_ns.route('/register/')
class RegistrationView(Resource):

    @auth_ns.response(404, "Нет данных")
    @auth_ns.response(201, "OK")
    @auth_ns.doc('Добавление нового пользователя в системц')
    def post(self):
        # Получаем данные
        data = request.json
        # Сериализуем
        serialized_data = UserSchema().load(data)
        email, password = serialized_data.get('email'), serialized_data.get('password')

        # Если есть None в одном из полей, то блокируем
        if None in [email, password]:
            return abort(404)

        # Выполняем добавление
        auth_service.create(serialized_data)

        return "", 201


@auth_ns.route('/login/')
class LoginView(Resource):

    @auth_ns.response(201, "OK")
    @auth_ns.response(404, "Нет данных")
    @auth_ns.response(500, "Ошибка")
    @auth_ns.doc('Осуществление входа пользователя. Выдача токенов')
    def post(self):
        try:
            # Получаем данные
            data = request.json

            # Сериализуем
            serialized_data = UserSchema().load(data)
            email, password = serialized_data.get('email'), serialized_data.get('password')

            # Если есть None в одном из полей, то блокируем
            if None in [email, password]:
                return abort(404, message='Нет данных')

            # Выполняем получение токенов
            tokens = auth_service.create_tokens(data)
            return tokens, 200

        except MarshmallowError as e:
            return f'Ошибка {e}', 500

        except TypeError as e:
            return f'Ошибка загрузки данных {e}', 500

    @auth_ns.doc('Обновление токенов')
    @auth_ns.response(204, "OK")
    @auth_ns.response(400, 'Ошибка! Отсутствует refresh_token')
    def put(self):
        # Получаем данные
        data = request.json
        # Получаем токен
        r_token = data.get('refresh_token')
        # Проверяем, что он не None
        if r_token is None:
            return {'error': 'Ошибка! Отсутствует refresh_token'}, 400

        tokens = auth_service.approve_token(r_token)
        return tokens, 200
