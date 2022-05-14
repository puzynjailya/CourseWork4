from marshmallow import fields, Schema


# Создаем схему сериализации для пользователей
class UserSchema(Schema):
    id = fields.Int(required=True, dump_only=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str()
    surname = fields.Str()
