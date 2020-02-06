from threading import Timer
import os
import json
import requests
import re
import fcntl
from requests.exceptions import ConnectionError

ko_target_path = os.path.join(
    os.path.dirname(__file__), '..', 'data/je_target_db.json')
scoring_path = os.path.join(os.path.dirname(
    __file__), '..', 'data/score_db.json')


def write_scores_to_file(scores):
  try:
    wf = open(scoring_path, 'w')
    wf.write(scores)
  finally:
    wf.close()
