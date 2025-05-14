from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with 
from flask_migrate import Migrate
from movieModel import db
from resources import MovieListResource

app = Flask(__name__)

#connect to a DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#initialize our db and our api
db.init_app(app)


#add migrations 
migrate = Migrate(app, db)

#add for API
api = Api(app)

# Create first tables
with app.app_context():
    db.create_all()

api.add_resource(MovieListResource, '/api/movies') 

@app.route('/')
def hello():
    return "Hello, Flask!"

@app.route('/movies')
def get_movies():
    return "List of movies"



if __name__ == '__main__':
    app.run(debug=True)



