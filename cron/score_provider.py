from threading import Timer
import os, json, requests, re
from requests.exceptions import ConnectionError

target_paths = os.path.join(
    os.path.dirname(__file__),'..' , 'data/target_db.json')
scoring_path = os.path.join(os.path.dirname(
    __file__), '..','data/score_db.json')


def get_scores():
  # Kick off timer here to continuously loop through KOTH endpoints for flags
  Timer(5, scores_cron).start()


def scores_cron():
  updates = []
  if (os.path.exists(target_paths)):
    rf = open(target_paths, 'r')
    try:
      file = rf.read()
      res = json.loads(file)

      for target in res:
        if target[:2] == 'KO':
          URL = res[target]['path']
          points = res[target]['score']
          # poll the game machine for flag
          try:
            res = requests.get(url=URL)
            body = res.text
          # parse the 'res' data here to get player info
            player = parse_koth_flag(body)
            if (player != ''):
              updates.append([player, target, points])
          except ConnectionError:
            pass

        if len(updates) > 0:
          post(updates)
    finally:
      rf.close()


def post(updates):
  new_scores = ''
  rf = open(scoring_path, 'r')
  try:
    file = rf.read()
    if len(file) > 0:
      # file exists with data
      current_score = json.loads(file)
      for i in updates:
        if i[0] in current_score.keys():
          score = 0
          player_obj = current_score[i[0]]['KO'][1:]
          for j in player_obj:
            found = False
            if j[0] == i[1]: #a score for this machine already exists for this player
              j[1] += 1
              score = i[2] * j[1]
              found = True
              break
          if found == False:
            player_obj.append([i[1], i[2], 1])
            score = i[2]
          current_score[i[0]]['KO'][0] = score
        else: #new player
          current_score[i[0]] = {'KO': [i[2], [i[1], i[2], 1]]}

      new_scores = json.dumps(current_score)
      write_scores_to_file(new_scores)
  finally:
    rf.close()


def write_scores_to_file(scores):
  try:
    wf = open(scoring_path, 'w')
    wf.write(scores)
  finally:
    wf.close()


def parse_koth_flag(body):
  team = re.search(r'<koth>(.*?)</koth>', body).group(1)
  return team
