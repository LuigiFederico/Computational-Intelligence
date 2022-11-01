def create_dict_genes(problem):
  id_to_genes = dict()
  id = 0

  for l in problem:
    id_to_genes[id] = Gene(id, l)
    id += 1
  
  return id_to_genes

# ----------------------------------------- #

class Gene:
  def __init__(self, id, values):
    self.id = id
    self.values = set(values)

  def __len__(self):
    return len(self.values)

  def __str__(self):
    return f'{self.values}'
  
  def display(self):
    print(f"{sorted(self.values)}")

