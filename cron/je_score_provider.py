from threading import Timer
import os
import json
import requests
import re
import fcntl
from requests.exceptions import ConnectionError

je_target_path = os.path.join(
    os.path.dirname(__file__), '..', 'data/je_target_db.json')
scoring_path = os.path.join(os.path.dirname(
    __file__), '..', 'data/score_db.json')

def _post(updates):
  ret_msg = 'error'
  valid = False
  dupe = False
  new_scores = ''
  rf = open(scoring_path, 'r')

  try:
    file = rf.read()

    if len(file) > 0:
      # file exists with data
      current_score = json.loads(file)

      if updates["team"] in current_score.keys(): # team is already on the board
        score = 0
        if "JE" in current_score[updates["team"]].keys():

          player_obj = current_score[updates["team"]]['JE'][1:]
          print("JE player_obj: ", player_obj)
          for item in player_obj:
            if item[0] == updates["id"]:
              dupe = True
              ret_msg = "Duplicate"
              break
          if dupe == False:
            # test for correct answer
            points = check_correct(updates["answer"], updates["id"])
            if ( points != False):
              # correct
              print("points: ", points)
              current_score[updates["team"]]["JE"][0] += points
              current_score[updates["team"]]["JE"].append([updates["id"], points])
              valid = True
              ret_msg = "Success"
            else:
              # incorrect
              ret_msg = "Incorrect"
        else: #first JE score
          points = check_correct(updates["answer"], updates["id"])
          if (points != False):
            current_score[updates["team"]]["JE"] = [points, [updates["id"], points]]
            valid = True
            ret_msg = "Success"
          else:
              ret_msg = "Incorrect"

      else: #new team on scoreboard
        points = check_correct(updates["answer"], updates["id"])
        if (points != False):
          current_score[updates["team"]]= {"JE": [
            points, [updates["id"], points]]}
          valid = True
          ret_msg = "Success"
        else:
            ret_msg = "Incorrect"

    if valid:
      new_scores = json.dumps(current_score)
      print("new scores", new_scores)
      write_scores_to_file(new_scores)

  finally:
    # write_scores_to_file('test')
    rf.close()
    return ret_msg




def write_scores_to_file(scores):
  print("got to write")
  try:
    wf = open(scoring_path, 'w')
    wf.write(scores)
    print("scores written")
  finally:
    wf.close()



def check_correct(answer, id):
  is_correct = False
  check_flags = open(je_target_path, 'r')
  try:
    flags = check_flags.read()
    all_flags = json.loads(flags)
    for flag in all_flags:
      print("flag: ", flag)
      print("id: ", id)
      if flag == id:
        print("match")
        print("solution: ", all_flags[flag]["solution"])
        print("answer: ", answer)
        if all_flags[flag]["solution"] == answer:
          is_correct = all_flags[flag]["score"]
          break
  finally:
    return is_correct


