from flask_restful import Resource, fields, marshal_with
from movieModel import db, Movie


#dict that tells the json what to look like
#serialize the movie object
movie_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'rating': fields.Float,
    'release_date': fields.Integer
}

class MovieListResource(Resource):
    @marshal_with(movie_fields)
    def get(self):
        #get all movies
        return Movie.query.all()