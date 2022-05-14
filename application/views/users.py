from flask import request, abort
from flask_restx import Namespace, Resource

from application.exceptions import ItemNotFound
from application.implemented import user_service, auth_service
from application.schemas.user import UserSchema
from application.utils import auth_required

user_ns = Namespace('users')


@user_ns.route('/<int:uid>/')
@user_ns.doc(params={'uid': 'ИД пользователя в БД'})
class UserView(Resource):

    @auth_required
    @user_ns.response(200, "OK")
    @user_ns.response(404, "User not found")
    def get(self, uid):
        try:
            result = user_service.get_user(user_id=uid)
            return result, 200
        except ItemNotFound:
            abort(404, message="Genre not found")

    @auth_required
    @user_ns.doc('Обновление данных пользователя (без пароля)')
    @user_ns.response(204, "OK")
    @user_ns.response(204, "OK")
    def patch(self, uid):

        # Получаем данные
        user_data = request.json
        user_data = UserSchema().load(user_data)
        if "id" not in user_data:
            user_data["id"] = uid
        # Запускаем сервис обновления
        user_service.update_userdata(user_data)
        return '', 204

    @auth_required
    @user_ns.doc('Обновление пароля пользователя')
    @user_ns.response(204, "OK")
    def put(self, uid):
        # Получаем данные о пароле в формате json
        # {"old_password": ,
        # "new_password": }

        passwords = request.json
        # Если данных нет хотя бы в одном из полей, то возвращаем ошибку 404
        if None in [passwords.get('old_password'), passwords.get('new_password')]:
            return abort(403)

        # Получаем токен пользователя
        user_data = request.headers['Authorization']
        token = user_data.split('Bearer ')[-1]

        user = user_service.update_userpass(token, passwords)
        new_tokens = auth_service.create_tokens(user)

        return new_tokens, 204



