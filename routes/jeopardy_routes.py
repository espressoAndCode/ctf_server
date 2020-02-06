from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse
import os, json
import cron.je_score_provider as jesp


class JeopardyRoutes(Resource):

  score_file = os.path.abspath('data/score_db.json')
  je_file = os.path.abspath('data/je_target_db.json')

  parser = reqparse.RequestParser()
  parser.add_argument("data")

  def get(self):
    if (os.path.exists(self.je_file)):
      with open(self.je_file, 'r') as f:
        file = f.read()
        res = json.loads(file)
        return res

  # this post only updates JE scores. KO scores are monitored internally
  # by 'ko_score_provider.py'

  def post(self):
    data = request.get_json(force=True)
    print("POST: ", data)
    if (os.path.exists(self.score_file)):
      with open(score_file, 'r') as rfile:
        pass
        # Check if there is already a score for this player/flag
        # if so, reply "Already have this flag"
        # if not, call the je_score_provider.write_scores_to_file method







        writefile.write(json.dumps(data))
    res = "Success"
    return res