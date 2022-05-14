from flask import request, abort
from flask_restx import Namespace, Resource

from application.exceptions import ItemNotFound
from application.implemented import genre_service

genres_ns = Namespace("genres")


@genres_ns.route("/")
class GenresView(Resource):

    @genres_ns.doc('Получение данных по всем жанрам')
    @genres_ns.response(200, "OK")
    def get(self):
        """Вьюшка получения всех жанров"""
        page = request.args.get('page')
        status = request.args.get('status')
        return genre_service.get_all_genres(page=page, status=status)


@genres_ns.route("/<int:genre_id>")
@genres_ns.doc(params={'genre_id': 'ИД жанра в БД'})
class GenreView(Resource):

    @genres_ns.doc('Получение данных по одному жанру')
    @genres_ns.response(200, "OK")
    @genres_ns.response(404, "Genre not found")
    def get(self, genre_id: int):
        """Вьюшка получения жанра по id"""
        try:
            return genre_service.get_item_by_id(genre_id), 200
        except ItemNotFound:
            abort(404, message="Genre not found")
