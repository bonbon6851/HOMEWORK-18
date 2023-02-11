import sqlalchemy
from flask import request
from flask_restx import Resource, Namespace
from implemented import movie_servise
from dao.model.movies import MovieSchema

movie_ns = Namespace('/movies')

movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
        Метод для обработки GET запроса для возвращения данных всех фильмов или с определенным фильтром
        """
        did = request.args.get('director_id')
        if did:
            return movie_schema.dump(movie_servise.get_by_director(did), many=True)

        gid = request.args.get('genre_id')
        if gid:
            return movie_schema.dump(movie_servise.get_by_genre(gid), many=True)

        year = request.args.get('year')
        if year:
            return movie_schema.dump(movie_servise.get_by_year(year), many=True)

        movies = movie_schema.dump(movie_servise.get_all(), many=True)
        if movies:
            return movies, 200

        return 'Фильм не найден', 404

    def post(self):
        data = request.json
        # Обработка исключения при попытке добавления записи с не уникальным primary key
        try:
            return movie_schema.dump(movie_servise.create(data)), 201
        except sqlalchemy.exc.IntegrityError as error:
            return f'{error}', 500


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        """
        Метод для обработки GET запроса для возвращения данных конкретного фильма
        """
        movie = movie_schema.dump(movie_servise.get_one(mid))
        if movie:
            return movie
        return f"Фильм с id {mid} не найден", 404

    def put(self, mid):
        """
        Метод для обработки PUT запроса на обновления данных фильма
        """
        data = request.json

        movie = movie_servise.get_one(mid)
        if movie:
            try:
                movie_schema.dump(movie_servise.update(mid, data))
                movie = movie_schema.dump(movie_servise.get_one(mid))
                return movie, 200
                # Обработка исключения при попытке обновления записи с не уникальным primary key
            except sqlalchemy.exc.IntegrityError as error:
                return f'{error}'
                # Обработка исключения при попытке обновления записи с не несоответствующими столбцами
            except sqlalchemy.exc.InvalidRequestError as error:
                return f'{error}'
        return f"Фильм с id {mid} не найден", 404

    def patch(self, mid):
        """
        Метод для обработки PATCH запроса на обновления данных фильма
        """
        data = request.json
        movie = movie_servise.get_one(mid)
        if movie:
            try:
                movie_schema.dump(movie_servise.update(mid, data))
                movie = movie_schema.dump(movie_servise.get_one(mid))
                return movie, 200
                # Обработка исключения при попытке обновления записи с не уникальным primary key
            except sqlalchemy.exc.IntegrityError as error:
                return f'{error}'
                # Обработка исключения при попытке обновления записи с не несоответствующими столбцами
            except sqlalchemy.exc.InvalidRequestError as error:
                return f'{error}'
        return f"Фильм с id {mid} не найден", 404

    def delete(self, mid):
        """
        Метод для обработки DELETE запроса для удаления конкретного фильма
        """
        movie = movie_servise.get_one(mid)
        if movie:
            return movie_schema.dump(movie_servise.delete(mid)), 204
        return f"Фильм с id {mid} не найден", 404
