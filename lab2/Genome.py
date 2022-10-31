from copy import deepcopy
import random
from Gene import Gene


class Genome:
  """
  Genome attributes:
  - genome: list of genes
  """

  def __init__(self, genes):
    self.genome = genes
  

  def __len__(self):
    len_ = 0
    for gene in self.genome:
      len_ += len(gene)  
    return len_


  def covered_values(self):
    covered = set()
    for gene in self.genome:
      covered |= gene.values
    
    return covered


  def cross_over(self, partner_genome, id_to_genes: dict):
    """
    returns the genome obtained from the crossover of the current genome
    with the genome of the partner individual
    """
    # randomly choose genes (choices between len(genome)//2 and len(genome))
    g_self = random.choices(self.genome,
                            k=random.randint(len(self.genome)//2, len(self.genome))) 
    g_parent = random.choices(self.genome,
                              k=random.randint(len(partner_genome)//2, len(partner_genome)))
    survivals = set([gene.id for gene in g_self + g_parent])

    return Genome([id_to_genes[g_id] for g_id in survivals])
  
  def smart_reproduction(self, partner_genome, id_to_genes: dict, N):
    # filter the duplicates ids -> exstract the candidate genes
    candidates = [id_to_genes[id_] for id_ in set([g.id for g in self.genome + partner_genome.genome])]

    stop = max(N, len(candidates))
    goal = set(range(N))
    covered = set()
    new_genome = list()

    for i in range(stop):
      best = max(candidates, key=lambda gene: len(goal) - len(covered | gene.values)) # max based on how much the gene would contribute to the solution
      new_genome.append(best)
      candidates.remove(best)
      if not candidates:
        break
    return Genome(new_genome)


  def mutate(self, id_to_genes: dict):
    genome = deepcopy(self.genome)
    point = random.randint(1, len(self.genome)-1)  # point of mutation
    candidates = set(id_to_genes.keys()) - set([gene.id for gene in self.genome]) # set of genes not present in self.genome
    
    genome[point] = id_to_genes[random.choice([c for c in candidates])] # Update the genome
    return Genome(genome)

    
