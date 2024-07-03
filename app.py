import os

from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv

from app import db
from app.resources import BarResource
from app.resources import BarModel

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

db.init_app(app)

api.add_resource(BarResource, '/bar/num_<int:id>', '/bar')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)