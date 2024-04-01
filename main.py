from random import randint
from timeit import Timer
from hashing import HashTable
from busca_binaria import ListaOrdenada
from busca_sequencial import ListaDesordenada

def gerar_pessoa():
    cpf = f"{randint(100000000, 999999999)}"
    nome = f"Pessoa {randint(1, 1000)}"
    telefone = "(XX) X XXXX-XXXX" 
    senha = "senha123"
    return Pessoa(cpf, nome, telefone, senha)

class Pessoa:
    def __init__(self, cpf, nome, telefone, senha):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.senha = senha

def main():
    tamanhos_dados = [10000, 100000, 1000000]

    estruturas = {
        "Hashing": HashTable,
        "Busca Binária": ListaOrdenada,
        "Busca Sequencial": ListaDesordenada
    }

    for tamanho_dados in tamanhos_dados:
        print(f"Tamanho do conjunto de dados: {tamanho_dados}")

        dados = [gerar_pessoa() for _ in range(tamanho_dados)]

        for estrutura, data_estrutura in estruturas.items():
            if estrutura == "Hashing":
                instancia = data_estrutura(tamanho_dados)
            else:
                instancia = data_estrutura()

            tempo_insercao = Timer(lambda instancia=instancia: [instancia.inserir(dado) for dado in dados]).timeit(number=1)
            print(f"  {estrutura}: {tempo_insercao:.10f} segundos (inserção)")
            tempo_medio_insercao = tempo_insercao / tamanho_dados
            print(f"  {estrutura}: {tempo_medio_insercao:.10f} tempo medio (inserção)")

            tempo_busca = Timer(lambda instancia=instancia: [instancia.buscar_por_cpf(dado.cpf) for dado in dados]).timeit(number=1)
            print(f"  {estrutura}: {tempo_busca:.10f} segundos (busca)")
            tempo_medio_busca = tempo_busca / tamanho_dados
            print(f"  {estrutura}: {tempo_medio_busca:.10f} segundos medio (busca)")

        print("---")

if __name__ == "__main__":
    main()
