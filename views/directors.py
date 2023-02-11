from flask_restx import Resource, Namespace
from dao.model.directors import DirectorSchema
from implemented import director_dao


director_ns = Namespace('/directors')

director_schema = DirectorSchema()


@director_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        return director_schema.dump(director_dao.get_all(), many=True)


@director_ns.route('/<int:did>')
class DirectorViews(Resource):
    def get(self, did):
        return director_schema.dump(director_dao.get_one(did))
