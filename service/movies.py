from dao.movies import MovieDAO


class MovieServise:
    def __init__(self, dao: MovieDAO):
        self.movie_dao = dao

    def get_one(self, mid):
        return self.movie_dao.get_one(mid)

    def get_all(self):
        return self.movie_dao.get_all()

    def get_by_director(self, did):
        return self.movie_dao.get_by_director(did)

    def get_by_genre(self, gid):
        return self.movie_dao.get_by_genre(gid)

    def get_by_year(self, year):
        return self.movie_dao.get_by_year(year)

    def create(self, data):
        return self.movie_dao.create(data)

    def update(self, mid, data):
        self.movie_dao.update(mid, data)

    def update_partial(self, data):
        self.movie_dao.update(data)

    def delete(self, mid):
        self.movie_dao.delete(mid)
