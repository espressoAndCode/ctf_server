#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, logging
from json import dumps

from routes.ko_routes import Scores
from routes.jeopardy_routes import JeopardyRoutes

app = Flask(__name__)
CORS(app, resources=r'*')
logging.getLogger('flask_cors').level = logging.DEBUG

app.config['DEBUG'] = True
api = Api(app)

#### ROUTES ####
api.add_resource(Scores, '/scores')
api.add_resource(JeopardyRoutes, '/jeopardy')


if __name__ == '__main__':
     app.run()
