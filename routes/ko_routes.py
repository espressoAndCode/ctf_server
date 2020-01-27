from flask_restful import Resource
import os, json
import cron.ko_score_provider as sp


class Scores(Resource):

  fn = os.path.abspath('data/score_db.json')
  def get(self):
    # sp.get_scores()
    if (os.path.exists(self.fn)):
      with open(self.fn, 'r') as f:
        file = f.read()
        res = json.loads(file)
        return res
