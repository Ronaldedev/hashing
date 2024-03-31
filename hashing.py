class HashTable:
  def __init__(self, tamanho):
    self.tabela = [[] for _ in range(tamanho)]

  def inserir(self, pessoa):
    indice = hash(pessoa.cpf) % len(self.tabela)
    self.tabela[indice].append(pessoa)

  def buscar_por_cpf(self, cpf):
    indice = hash(cpf) % len(self.tabela)
    for pessoa in self.tabela[indice]:
      if pessoa.cpf == cpf:
        return pessoa
    return None
