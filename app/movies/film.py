from typing import Dict, List
from werkzeug.exceptions import BadRequest
from cerberus import Validator
from app.settings.schema import MOVIE_SCHEMA
##from app import app_db


class Film:
    def get_all(self) -> List:
        """ Returns a list of all movies
        """
        return "test"
##    app_db.find_many()

##    def search_by_name(self, movie_name: str) -> List:
##        """ TODO: returns a list of movies that match by name
##        """
##        query = {
##            "movie": {  # field name
##                "$regex": rf"{movie_name}",  # regex filter
##                "$options": 'i'  # case-insensitive
##            }
##        }
##        return app_db.find_many(query)
##
##    def add(self, new_movie: Dict) -> Dict:
##        """ Add a new movie
##        """
##        validator = Validator(MOVIE_SCHEMA)
##        if not validator.validate(new_movie):
##            raise BadRequest(validator.errors)
##        _id = app_db.insert_one(new_movie)
##        new_movie.update({'_id': _id})
##        return new_movie
##
##    def delete_by_name(self, movie_name: str) -> None:
##        """ TODO: Delete movies that match name
##        """
##        query = {
##            "movie": movie_name
##        }
##        return app_db.delete_one(query)
##
