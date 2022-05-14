from flask import request
from flask_restx import Resource, Namespace, abort

from application.exceptions import ItemNotFound
from application.implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):

    @movie_ns.doc('Получение данных по всем фильмам')
    @movie_ns.response(200, "OK")
    def get(self):

        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        page = request.args.get("page")
        status = request.args.get("status")

        result = movie_service.get_all(director, genre, year, page, status)
        return result, 200

    @movie_ns.doc('Добавление фильма в БД')
    @movie_ns.response(201, "Created")
    def post(self):
        req_json = request.json
        movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:bid>')
@movie_ns.doc(params={'genre_id': 'ИД фильма в БД'})
class MovieView(Resource):

    @movie_ns.doc('Получение данных по одному фильму')
    @movie_ns.response(200, "OK")
    @movie_ns.response(404, "Movie not found")
    def get(self, bid):
        try:
            result = movie_service.get_one(bid)
            return result, 200
        except ItemNotFound:
            movie_ns.abort(404, message="Movie not found")

    @movie_ns.doc('Обновление данных фильма')
    @movie_ns.response(204, "OK")
    def put(self, bid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    @movie_ns.doc('Удаление  фильма')
    @movie_ns.response(204, "OK")
    def delete(self, bid):
        movie_service.delete(bid)
        return "", 204
