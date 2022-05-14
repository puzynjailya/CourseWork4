import json
from application.config import BaseConfig
import jwt
from flask import request, abort


def read_json(filename, encoding="utf-8"):
    with open(filename, encoding=encoding) as f:
        return json.load(f)


def auth_required(func):
    # Создаем обертку
    def wrapper(*args, **kwargs):
        # Проверяем наличие авторазации в заголовках
        if 'Authorization' not in request.headers:
            abort(401, 'Нельзя попасть в систему без авторизации')

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.PWD_JWT_ALGO])
        except Exception as e:
            abort(401, f'Упс, что-то пошло совсем не так \n {e}')
        return func(*args, **kwargs)
    return wrapper
