from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)  
    release_date = db.Column(db.Integer, nullable=False)

#allows for the creation of a new movie we can see based on the parameters below
    def __repr__(self):
        return f"<Movie {self.id} {self.title} {self.description} {self.release_date} {self.rating}>" 

