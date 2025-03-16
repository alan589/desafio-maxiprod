from pessoa import Pessoa
from transacao import Transacao
from prettytable import PrettyTable

class Cadastro:

    def __init__(self):
        # inicializa variáveis
        self.identificador_pessoa = 0
        self.identificador_transacao = 0
        self.pessoas = []
        self.transacoes = []
        self.table = PrettyTable()

    def exibir_cadastrados(self):
        """
        Exibe todos cadastrados.
        """
        print("\n\n\n")

        # adiciona os cabeçalhos id, nome e idade na tabela
        self.table.field_names = ["#ID", "Nome", "Idade"]

        # adiciona as linhas
        for pessoa in self.pessoas:
            self.table.add_row([pessoa.pessoa_id, pessoa.nome, pessoa.idade])

        # exibe a tabela
        print(self.table)

        # limpa a tabela
        self.table.clear()


    def consultar_total(self):
        """
        Exibe receita, despesas e saldo de todos os cadastrados.
        """
        print("\n\n\n")
        total_receita = 0
        total_despesa = 0
        receitas = []
        despesas = []

        # cria uma tabela com cabeçalhos
        self.table.field_names = ["#ID", "Nome", "Total receitas", "Total despesas", "Saldo"]

        # pecorre as listas transacao e pessoas
        for pessoa in self.pessoas:
            for transacao in self.transacoes:
                # verifica se id da pessoa é igual id da transacao
                if pessoa.pessoa_id == transacao.pessoa_id:
                    # se for do tipo receita soma o valor a variavel total_receita
                    if transacao.tipo == "receita":
                        total_receita += transacao.valor
                    # senão adiciona ao total_despesa
                    else:
                        total_despesa += transacao.valor
            # quando o for transacao chega ao fim, adiciona uma linha na tabela com os dados da pessoa e receita.
            self.table.add_row([pessoa.pessoa_id, pessoa.nome, total_receita, total_despesa, total_receita - total_despesa])

            # coloca numa lista os totais e zera as variaveis
            receitas.append(total_receita)
            despesas.append(total_despesa)
            total_receita = 0
            total_despesa = 0

        # formata a tabela e coloca mais uma linha
        self.table.float_format = "0.2"
        self.table.align = "r"
        self.table.add_divider()
        self.table.add_row(["", "", "Total", "Total", "Saldo"])
        self.table.add_divider()

        # soma todas as receitas e despesas
        soma_receitas = sum(receitas)
        soma_despesas = sum(despesas)
        # adiciona mais uma linha na tabela
        self.table.add_row(["", "", soma_receitas, soma_despesas, soma_receitas - soma_despesas])

        # imprimi e limpa tabela
        print(self.table)
        self.table.clear()

    def deletar_pessoa(self):
        """
        Deleta pessoa e suas transações do cadastro.
        """
        # entrada do id
        p_id = int(input("Id: "))

        # pecorre a lista pessoas
        for pessoa in self.pessoas:
            # caso encontre o id remove da lista
            if pessoa.pessoa_id == p_id:
                # pecorre a lista transacoes
                for transacao in self.transacoes.copy():
                    # se o id pessoa igualar o id da transacao remove da lista
                    if transacao.pessoa_id == p_id:
                        self.transacoes.remove(transacao)
                self.pessoas.remove(pessoa)
                print(f"\nVocê removeu {pessoa.nome}.")
                return

    def cadastrar_pessoa(self):
        """
        Cadastra uma pessoa com nome e idade.
        """
        print("\n")
        # entrada dos dados
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        self.pessoas.append(Pessoa(self.identificador_pessoa, nome, idade))
        self.identificador_pessoa += 1
        print("\nCadastro realizado!")

    def cadastrar_transacao(self):
        """
        Cadastra uma transação com descricao, valor e tipo.
        Caso o identificador da pessoa não exista retorna uma mensagem negativa.
        """
        print("\n")
        # entrada dos dados
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))
        tipo = input("Tipo(despesa/receita): ")
        pessoa_id = int(input("Identificador da pessoa: "))

        # se for menor de idade e o tipo for ''receita' retorna ao programa principal
        menor_idade = self.verificar_menor_idade(pessoa_id)
        if menor_idade and tipo == "receita":
            print("\nSomente despesa é aceito para menores de 18 anos.")
            return

        # verifica se o identificador existe na lista pessoas
        existe = self.verificar_identificador(pessoa_id)
        # se existir, cria uma transação e adiciona na lista transações, caso contrário retorna uma mensagem negativa
        if existe:
            self.transacoes.append(Transacao(self.identificador_transacao, descricao, valor, tipo, pessoa_id))
            self.identificador_transacao += 1
            print("\nCadastro realizado!")
        else:
            print("\nIdentificador inválido.")

    def verificar_menor_idade(self, pessoa_id):
        """
        Verifica se uma pessoa é menor de idade, se sim retorna True, o contrário retorna False
        """

        for pessoa in self.pessoas:
            if pessoa.pessoa_id == pessoa_id and pessoa.idade < 18:
                return True
        return False

    def verificar_identificador(self, identificador):
        """
        Verifica se um identificador existe, caso exista retorna True senão False.
        """
        for pessoa in self.pessoas:
            if pessoa.pessoa_id == identificador:
                return True
        return False