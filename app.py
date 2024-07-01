from flask import Flask
from flask_restful import Api

from app import db
from app.resources import BarResource
from app.resources import BarModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/krasnodarbars'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

db.init_app(app)

api.add_resource(BarResource, '/bar/num_<int:id>', '/bar')

if __name__ == '__main__':
    app.run()