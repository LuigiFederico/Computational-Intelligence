import random
import logging
from copy import deepcopy
from nim import Nimply, Nim


def nim_sum(elem: list):
  x = 0
  for e in elem:
    x = e ^ x
  return x

##################
##  STRATEGIES  ##
##################

# Level 0: Easy
def dumb_action(nim: Nim):
  """
  Always takes one obj from the first row available
  """
  row = [r for r, n in enumerate(nim._rows) if n > 0][0]
  return Nimply(row, 1)


# Level 1: Medium
def dumb_random_action(nim: Nim):
  """
  There is 0.5 of probability to make a dumb action or a random action
  """
  if random.random() < 0.5:
    return dumb_action(nim)
  else: return random_action(nim)


# Level 2: Medium-Advanced
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


# Level 3: Medium-Advanced
def layered_action(nim: Nim):
  """
  Always takes the whole row's objs choosing randomly the row
  """
  row, num_obj = random.choice([(r, n) for r, n in enumerate(nim._rows) if n > 0])
  if nim._k and num_obj > nim._k:
    return Nimply(row, nim._k)
  return Nimply(row, num_obj)


# Level 4: DEMIGOD 
def demigod_action(nim: Nim, prob_god=0.5):
  """
    There is a probability prob to play an expert move and a chance to play randomly
  """
  if random.random() < prob_god:
    return expert_action(nim)
  else: return random_action(nim)

  
# Level 5: GOD 
def expert_action(nim: Nim):
  """
    The agent uses fixed rules based on nim-sum (expert-system)

    Returns the index of the pile and the number of pieces removed as a Nimply namedtuple
  """
  board = nim._rows
  k = nim._k

  # Winning move if there is only one row left
  tmp = [(i, r) for i, r in enumerate(board) if r > 0]
  if len(tmp) == 1:
    row, num_obj = tmp[0]
    if not k or num_obj <= k:
      return Nimply(row, num_obj) # Take the entire row


  # Compute the nim-sum of all the heap sizes
  x = nim_sum(board)

  if x > 0:
    # Current player on a insucure position -> is winning
    # --> Has to generate a secure position (bad for the other player)
    # --> Find a heap where the nim-sum of X and the heap-size is less than the heap-size.
    # --> Then play on that heap, reducing the heap to the nim-sum of its original size with X
    
    good_rows = [] # A list is needed because of k
    for row, row_size in enumerate(board):
      if row_size == 0:
        continue
      ns = row_size ^ x # nim sum
      if ns < row_size:
        good_rows.append((row, row_size)) # This row will have nim sum = 0
        
    for row, row_size in good_rows:
      board_tmp = deepcopy(board)
      for i in range(row_size):
       board_tmp[row] -= 1 
       if nim_sum(board_tmp) == 0:  # winning move
        num_obj = abs(board[row] - board_tmp[row])
        if not k or num_obj <= k:
          return Nimply(row, num_obj)
  
  # x == 0 or k force a bad move to the player
  # Current player on a secure position or on a bad position bc of k -> is losing
  # --> Can only generate an insicure position (good for the other player)
  # --> Perform a random action bc it doesn't matter
  return random_action(nim)
  

opponents = {
  1: dumb_action,
  2: dumb_random_action,
  3: random_action,
  4: layered_action,
  5: demigod_action,
  6: expert_action
}



####################
##  PLAY MATCHES  ##
####################

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
      logging.debug(f'Action P{player} = {ply}')
      nim_tmp.nimming(ply)
      logging.debug(f'player {player} -> {nim_tmp}\tnim_sum = {nim_sum(nim_tmp._rows)}')

    logging.debug(f'\n### Player {player} won ###\n')
    if player == 0:
      won += 1
      
  return won/n_matches


