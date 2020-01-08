from flask_restful import Resource
import os, json



class Scores(Resource):
  fn = os.path.abspath('data/score_db.json')
  def get(self):
    if (os.path.exists(self.fn)):
      with open(self.fn, 'r') as f:
        file = f.read()
        res = json.loads(file)
        return res


  def post (self, data):
    pass
    # with open(fn, 'a+') as writefile:
    #   writefile.write(json.dumps(data))

