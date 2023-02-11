from service.movies import MovieServise
from service.directors import DirectorServise
from service.genres import GenreServise
from setup_db import db
from dao.movies import MovieDAO
from dao.directors import DirectorDAO
from dao.genres import GenreDAO

movie_dao = MovieDAO(db.session)
movie_servise = MovieServise(dao=movie_dao)

director_dao = DirectorDAO(db.session)
director_servise = DirectorServise(dao=director_dao)

genre_dao = GenreDAO(db.session)
genre_servise = GenreServise(dao=genre_dao)
