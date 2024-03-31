class ListaDesordenada:
  def __init__(self):
    self.dados = []

  def inserir(self, pessoa):
    self.dados.append(pessoa)

  def buscar_por_cpf(self, cpf):
    for pessoa in self.dados:
      if pessoa.cpf == cpf:
        return pessoa
    return None
