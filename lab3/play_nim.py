import random
import logging
from copy import deepcopy
from nim import Nimply, Nim


def nim_sum(elem: list):
  x = 0
  for e in elem:
    x = e ^ x
  return x


def random_action(nim: Nim):
  """
    The agent performs a random action
  """
  row = random.choice([r for r, n in enumerate(nim._rows) if n > 0])
  if nim._k:
    num_obj = random.randint(1, min(nim._k, nim._rows[row]))
  else:
    num_obj = random.randint(1, nim._rows[row])
  
  return Nimply(row, num_obj)



def evaluate(nim: Nim, n_matches=20, *, my_action, opponent_action=random_action, debug=False):
  """
    This function let you evaluate how many matches your strategy wins against an opponent.  
    You are player 0.  

    Input:
      - nim: Nim
      - n_matches=20
      - my_action
      - opponent_action=random_action
      - debug=False # let's you display all the match moves for each match

    Output:
      - Percentage of won matches (number of wins / number of matches)
  """
  
  if debug:
    logging.getLogger().setLevel(logging.DEBUG)

  player_action = {
    0: my_action, # our champion
    1: opponent_action # our opponent
    }

  won = 0

  for m in range(n_matches):
    # Setup match
    nim_tmp = deepcopy(nim)
    if m/n_matches > 0.5:
      player = 1  # You start
    else:
      player = 0  # Opponent starts

    logging.debug(f'Board -> {nim_tmp}\tk = {nim_tmp._k}')
    logging.debug(f'Player {1-player} starts\n')
    
    # Play the match
    while not sum(nim_tmp._rows) == 0:
      player = 1 - player
      ply = player_action[player](nim_tmp)
      nim_tmp.nimming(ply)
      logging.debug(f'player {player} -> {nim_tmp}\tnim_sum = {nim_sum(nim_tmp._rows)}')

    logging.debug(f'\n### Player {player} won ###\n')
    if player == 0:
      won += 1
      
  return won/n_matches