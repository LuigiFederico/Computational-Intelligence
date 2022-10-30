from collections import namedtuple
from Genome import Genome

Cost = namedtuple("Cost", ["n_vals", "healty" ,"length"])

class Individual:
  """
  Individual:
  - genome = list of genes
  - covered: set of covered values between 0 and N-1
  - fitness: tuple of two elements representing the quality of the individual
    - n_vals: Number of distinct values covered (the higher, the better; max equal to N)
    - lenght: Total length of the genome (sum of lenghts of the genes)
  """
  def __init__(self, genome):
    self.genome = genome    # list of genes
    self.covered = genome.covered_values() # set
    self.fitness = Cost(len(genome.covered), -len(genome))
    

  def is_healty(self, N):
    """
      The individual is healty if it's genome contains
      all the numbers between 0 and N-1.
    """
    return len(self.covered) == N

  def fight(self, opponent):
    return max(self.fitness, opponent.fitness)
