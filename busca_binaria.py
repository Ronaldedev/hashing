class ListaOrdenada:
  def __init__(self):
    self.dados = []

  def inserir(self, pessoa):
    indice = self.buscar_indice_insercao(pessoa.cpf)
    self.dados.insert(indice, pessoa)

  def buscar_indice_insercao(self, cpf):
    baixo, alto = 0, len(self.dados) - 1
    while baixo <= alto:
      meio = (baixo + alto) // 2
      if self.dados[meio].cpf == cpf:
        return meio
      elif self.dados[meio].cpf < cpf:
        baixo = meio + 1
      else:
        alto = meio - 1
    return baixo 

  def buscar_por_cpf(self, cpf):
    baixo, alto = 0, len(self.dados) - 1
    while baixo <= alto:
      meio = (baixo + alto) // 2
      if self.dados[meio].cpf == cpf:
        return self.dados[meio]
      elif self.dados[meio].cpf < cpf:
        baixo = meio + 1
      else:
        alto = meio - 1
    return None
