def create_dict_genes(problem):
  id_to_genes = dict()
  id = 0

  for l in problem:
    g = Gene(id, l)
    id_to_genes[id] = g
    id += 1
  
  return id_to_genes

# ----------------------------------------- #

class Gene:
  def __init__(self, id, values):
    self.id = id
    self.values = set(values)

  def __len__(self):
    return len(self.values)
    

