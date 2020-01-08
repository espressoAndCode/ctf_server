from threading import Timer
import os, json, requests

target_paths = os.path.join(
    os.path.dirname(__file__),'..' , 'data/target_db.json')
scoring_path = os.path.join(os.path.dirname(
    __file__), '..','data/score_db.json')
print("scoring path: ", scoring_path)

def get_scores():

  updates = []
  if (os.path.exists(target_paths)):
    with open(target_paths, 'r') as rf:
      file = rf.read()
      res = json.loads(file)

      for target in res:
        if target[:2] == 'KO':
          URL = res[target]['path']
          points = res[target]['score']
          # poll the game machine for flag
          # res = requests.get(url=URL)

          # parse the 'res' data here to get player info
          player = "DC864" #mock data

          if (player != ''):
            updates.append([player, target, points])

      if len(updates) > 0:
        post(updates)


      Timer(5, get_scores).start()


def post(updates):
  print("updates: ", updates)

  with open(scoring_path, 'r') as rf:
    file = rf.read()
    if len(file) > 0:
      # file exists with data
      current_score = json.loads(file)
      for i in updates:
        if i[0] in current_score.keys():
          print("Key found")
          score = 0
          player_obj = current_score[i[0]]['KO'][1:]
          print("player_obj: ", player_obj)
          for j in player_obj:
            found = False
            if j[0] == i[1]: #a score for this machine already exists for this player
              j[2] += 1
              score = i[2] * j[2]
              found = True
              break
          if found == False:
            player_obj.append([i[1], i[2], 1])
            score = i[2]

        current_score[i[0]]['KO'][0] += score
        print(score)


    else:
      pass #score_db does not exist or is empty - need to create and append updates


    # TODO:
    #   Create an object that holds ALL existing and updated scores
    #   once all updates are recorded, call write_scores_to_file with it as argument
        # so we are only writing the file once



def write_scores_to_file(scores):
  pass
  # with open(scoring_path, 'w') as wf:
  #   wf.write(json.dumps(scores))

get_scores()
