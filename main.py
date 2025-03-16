####################################################################
#                                                                  #
#                                                                  #
# Para executar o projeto siga os passos a seguir:                 #
# Instale python                                                   #
# Execute install.py para instalar as dependências                 #
# Execute main.py                                                  #
#                                                                  #
#                                                                  #
####################################################################

from cadastro import Cadastro
from logo import logo

cadastro = Cadastro()
escolha = -1

print(logo)
# executa o trecho dentro do while enquanto 'escolha' for diferente de 0
while escolha != 0:
    print("""
    1- Cadastrar pessoa
    2- Deletar pessoa
    3- Cadastrar transação
    4- Consultar total
    5- Exibir cadastrados
    0- Sair
    """)

    # se o usuário colocar um valor incompátivel lança uma exceção
    try:
        escolha = int(input(": "))

        if escolha == 1:
            cadastro.cadastrar_pessoa()
        elif escolha == 2:
            cadastro.deletar_pessoa()
        elif escolha == 3:
            cadastro.cadastrar_transacao()
        elif escolha == 4:
            cadastro.consultar_total()
        elif escolha == 5:
            cadastro.exibir_cadastrados()
    except ValueError:
        print("\n\nColoque uma entrada válida.\n\n")




