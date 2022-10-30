import random
from Gene import Gene




class Genome:
  """
  Genome attributes:
  - genome: list of genes
  - mut_rate: mutation probability of the genome
  
  """

  def __init__(self, genes: list(Gene), mut_rate=0.1):
    self.mut_rate = mut_rate
    self.genome = genes
  

  def __len__(self):
    len_ = 0
    for gene in self.genome:
      len_ += len(gene)  
    return len_


  def set_mut_rate(self, mut_rate):
    self.mut_rate = mut_rate


  def covered_values(self):
    covered = set()
    for gene in self.genome:
      covered |= gene.values
    
    return covered


  def cross_over(self, partner_genome: list(Gene), id_to_genes: dict):
    """
    returns the genome obtained from the crossover of the current genome
    with the genome of the partner individual
    """
    # randomly choose genes (choices between len(genome)//2 and len(genome))
    g_self = random.choices(self.genome,
                            k=random.randint(len(self.genome)//2, len(self.genome))) 
    g_parent = random.choices(self.genome,
                              k=random.randint(len(partner_genome//2, len(partner_genome))))
    survivals = set([gene.id for gene in g_self + g_parent])

    return Genome([id_to_genes[g_id] for g_id in survivals])
  

  def mutation(self, id_to_genes: dict):
    """ Changes a gene on a random point inside the genome with probability equal to self.mut_rate"""
    if random.random() < self.mut_rate:
      point = random.randint(0, len(self.genome)-1)  # point of mutation
      candidates = set(id_to_genes.keys()) - set([gene.id for gene in self.genome]) # set of genes not present in self.genome
      
      self.genome[point] = id_to_genes[random.choice(candidates)] # Update the genome

