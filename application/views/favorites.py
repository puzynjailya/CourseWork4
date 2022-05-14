from flask import request
from flask_restx import Namespace, Resource

from application.implemented import favorite_service, movie_service, genre_service
from application.utils import auth_required

favorites_ns = Namespace('favorites')


@favorites_ns.route('/movies/<int:mid>')
class FavoriteMoviesCBV(Resource):

    @auth_required
    def post(self, mid):
        # Получаем данные о пользователе:
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        movie = movie_service.get_one(mid, return_obj=True)
        favorite_service.add_favorite(token, movie, movie_flag=True)
        return '', 201

    @auth_required
    def delete(self, mid):
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        movie = movie_service.get_one(mid, return_obj=True)
        favorite_service.remove_favorite(token, movie, movie_flag=True)
        return '', 204


@favorites_ns.route('/genres/<int:gid>')
class FavoriteGenresCBV(Resource):

    @auth_required
    def post(self, gid):
        # Получаем данные о пользователе:
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        genre = genre_service.get_item_by_id(gid, return_obj=True)
        favorite_service.add_favorite(token, genre, movie_flag=False)
        return '', 201

    @auth_required
    def delete(self, gid):
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        genre = genre_service.get_item_by_id(gid, return_obj=True)
        favorite_service.remove_favorite(token, genre, movie_flag=False)
        return '', 204
