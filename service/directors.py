from dao.directors import DirectorDAO


class DirectorServise:
    def __init__(self, dao: DirectorDAO):
        self.director_dao = dao

    def get_one(self, did):
        return self.director_dao.get_one(did)

    def get_all(self):
        return self.director_dao.get_all()
