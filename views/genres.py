from flask_restx import Resource, Namespace
from dao.model.genres import GenreSchema
from implemented import genre_dao

genre_ns = Namespace('/genres')

genre_schema = GenreSchema()


@genre_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        return genre_schema.dump(genre_dao.get_all(), many=True)


@genre_ns.route('/<int:gid>')
class DirectorViews(Resource):
    def get(self, gid):
        return genre_schema.dump(genre_dao.get_one(gid))
