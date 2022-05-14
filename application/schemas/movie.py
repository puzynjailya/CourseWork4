from marshmallow import fields, Schema


# Создаем схему сериализации для фильмов
class MovieSchema(Schema):
    id = fields.Int(dump_only=True, required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    trailer = fields.Str(required=True)
    year = fields.Int(required=True)
    rating = fields.Int(required=True)

    # Создаем связи с жанрами
    genre_id = fields.Int(required=True)
    # genre = fields.Nested("Genre")

    # Создаем связи с режиссерами
    director_id = fields.Int(required=True)
    # director = fields.Nested("Director")
