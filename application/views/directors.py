from flask import request, abort
from flask_restx import Resource, Namespace

from application.schemas.director import DirectorSchema
from application.implemented import director_service
from application.exceptions import ItemNotFound

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):

    @director_ns.doc('Получение данных по всем режиссерам')
    @director_ns.response(200, "OK")
    def get(self):
        page = request.args.get("page")
        status = request.args.get("status")
        rs = director_service.get_all_directors(page=page, status=status)
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@director_ns.route('/<int:rid>')
@director_ns.doc(params={'rid': 'ИД режиссера в БД'})
class DirectorView(Resource):

    @director_ns.doc('Получение данных по одному режиссеру')
    @director_ns.response(200, "OK")
    @director_ns.response(404, "Director not found")
    def get(self, rid):
        try:
            r = director_service.get_one(rid)
            sm_d = DirectorSchema().dump(r)
            return sm_d, 200
        except ItemNotFound:
            director_ns.abort(404, message="Director not found")
