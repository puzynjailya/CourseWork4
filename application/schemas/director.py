from marshmallow import fields, Schema


# Создаем схему сериализации для режиссеров
class DirectorSchema(Schema):
    id = fields.Int(dump_only=True, required=True)
    name = fields.Str(required=True)
