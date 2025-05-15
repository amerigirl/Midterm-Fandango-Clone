from flask_restful import Resource, reqparse, fields, marshal_with
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

movie_params = reqparse.RequestParser()
movie_params.add_argument('title', type=str, help='Title of the movie is required', required=True) 
movie_params.add_argument('description', type=str, help='Description of the movie is required', required=True)
movie_params.add_argument('rating', type=float, help='Rating of the movie is required', required=True)        
movie_params.add_argument('release_date', type=int, help='Release date of the movie is required', required=True)
class MovieListResource(Resource):
    @marshal_with(movie_fields)
    def get(self):
        #get all movies
        return Movie.query.all()
    
    @marshal_with(movie_fields)
    def post(self):
        params = movie_params.parse_args()
        new_movie = Movie(
            title=params.get('title'),
            description=params.get('description'),
            rating=params.get('rating'),
            release_date=params.get('release_date')
        )
        # Add the new movie to the session and commit
        db.session.add(new_movie)
        db.session.commit()
        return new_movie, 201
