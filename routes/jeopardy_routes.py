from flask_restful import Resource
import os
import json


class JeopardyRoutes(Resource):

  score_file = os.path.abspath('data/score_db.json')
  je_file = os.path.abspath('data/je_target_db.json')

  def get(self):
    if (os.path.exists(self.je_file)):
      with open(self.je_file, 'r') as f:
        file = f.read()
        res = json.loads(file)
        return res

  # this post only updates JE scores. KO scores are monitored internally
  # by 'ko_score_provider.py'

  def post(self, data):
    print("POST: ", data)
    if (os.path.exists(self.score_file)):
      with open(score_file, 'w+') as writefile:
        writefile.write(json.dumps(data))
