from dao.genres import GenreDAO


class GenreServise:
    def __init__(self, dao: GenreDAO):
        self.genre_dao = dao

    def get_one(self, gid):
        return self.genre_dao.get_one(gid)

    def get_all(self):
        return self.genre_dao.get_all()
