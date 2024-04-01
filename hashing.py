class HashTable:
  def __init__(self, tamanho):
    self.dados = [[] for _ in range(tamanho)]

  def inserir(self, pessoa):
    indice = hash(pessoa.cpf) % len(self.dados)
    self.dados[indice].append(pessoa)

  def buscar_por_cpf(self, cpf):
    indice = hash(cpf) % len(self.dados)
    for pessoa in self.dados[indice]:
      if pessoa.cpf == cpf:
        return pessoa
    return None
