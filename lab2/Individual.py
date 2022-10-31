from collections import namedtuple
from Genome import Genome

W_FACTOR = 2
INTW_FACTOR = 10

class Individual:
  """
  Individual:
  - genome = list of genes
  - covered: set of covered values between 0 and N-1
  - fitness: weighted number of digits left to find the goal state + the weighted len of the list
  """
  def __init__(self, genome: Genome, N):
    self.genome = genome    # list of genes
    self.covered = genome.covered_values() # set
    goal = set(range(N))
    self.cost = len(genome) * W_FACTOR + len(goal - self.covered) * INTW_FACTOR

  def __len__(self):
    return len(self.genome)    

  def is_healty(self, N):
    """
      The individual is healty if it's genome contains
      all the numbers between 0 and N-1.
    """
    return len(self.covered) == N

  
  def fight(self, opponent):
    if self.cost < opponent.cost:
      return self
    else:
      return opponent
  

  #def reproduce(self, partner, id_to_genes: dict):
  #  return Individual(self.genome.cross_over(partner.genome, id_to_genes))

  def reproduce(self, partner, id_to_genes, N):
      return Individual(self.genome.smart_reproduction(partner.genome, id_to_genes, N), N)
  
  def mutate(self, id_to_genes, N):
    return Individual(self.genome.mutate(id_to_genes), N)