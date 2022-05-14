from marshmallow import fields, Schema


# Создаем схему сериализации для Жанров
class GenreSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
