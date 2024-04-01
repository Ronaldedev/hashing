from random import randint
from timeit import Timer
from hashing import HashTable
from busca_binaria import ListaOrdenada
from busca_sequencial import ListaDesordenada

def gerar_pessoa():
  #Gera uma pessoa aleatória
  cpf = f"{randint(100000000, 999999999)}"  # Gera CPF com 11 dígitos
  nome = f"Pessoa {randint(1, 1000)}"
  telefone = f"(XX) X XXXX-XXXX"  # Formato de telefone brasileiro
  senha = "senha123"  # Senha temporária
  return Pessoa(cpf, nome, telefone, senha)

class Pessoa:
  def __init__(self, cpf, nome, telefone, senha):
    self.cpf = cpf
    self.nome = nome
    self.telefone = telefone
    self.senha = senha

def main():

  # Tamanho dos conjuntos de dados para teste
  tamanhos_dados = [10000, 100000, 1000000]

  # Estruturas de dados
  estruturas = {
      "Hashing": HashTable(10000),  # Ajuste o tamanho inicial da tabela hash
      "Busca Binária": ListaOrdenada(),
      "Busca Sequencial": ListaDesordenada()
  }

  # Loop pelos tamanhos dos dados
  for tamanho_dados in tamanhos_dados:
    print(f"Tamanho do conjunto de dados: {tamanho_dados}")

    # Geração de dados aleatórios
    dados = [gerar_pessoa() for _ in range(tamanho_dados)]

    # Inserção de dados (teste de performance)
    for estrutura, data_estrutura in estruturas.items():
      tempo_insercao = Timer(lambda data_estrutura=data_estrutura: [data_estrutura.inserir(dado) for dado in dados]).timeit(number=1)
      tempo_medio_insercao = tempo_insercao / tamanho_dados
      print(f"  {estrutura}: {tempo_medio_insercao:.10f} segundos (inserção)")

    # Busca de dados (teste de performance)
    for estrutura, data_estrutura in estruturas.items():
      # Insira todos os dados na estrutura antes de iniciar a medição de busca
      for dado in dados:
        data_estrutura.inserir(dado)
      tempo_busca = Timer(lambda data_estrutura=data_estrutura: [data_estrutura.buscar_por_cpf(dado.cpf) for dado in dados]).timeit(number=1)
      tempo_medio_busca = tempo_busca / tamanho_dados
      print(f"  {estrutura}: {tempo_medio_busca:.10f} segundos (busca)")

    print("---")

if __name__ == "__main__":
  main()
