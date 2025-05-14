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

movie_args = reqparse.RequestParser()
movie_args.add_argument('title', type=str, help='Title of the movie is required', required=True) 
movie_args.add_argument('description', type=str, help='Description of the movie is required', required=True)
movie_args.add_argument('rating', type=float, help='Rating of the movie is required', required=True)        

class MovieListResource(Resource):
    @marshal_with(movie_fields)
    def get(self):
        #get all movies
        return Movie.query.all()
    
    @marshal_with(movie_fields)
    def post(self):
        args = movie_args.parse_args()
        new_movie = Movie(
            title=args['title'],
            description=args['description'],
            rating=args['rating'],
            release_date=args['release_date']
        )
        # Add the new movie to the session and commit
        db.session.add(new_movie)
        db.session.commit()
        return new_movie.query.all()