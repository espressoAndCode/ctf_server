#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps

from routes.scores import Scores

app = Flask(__name__)
app.config['DEBUG'] = True
api = Api(app)

#### ROUTES ####
api.add_resource(Scores, '/scores')


if __name__ == '__main__':
     app.run()