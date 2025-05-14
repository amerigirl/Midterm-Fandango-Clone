from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)
api = Api(app)


@app.route('/')
def hello():
    return "Hello, Flask!"





if __name__ == '__main__':
    app.run(debug=True)



