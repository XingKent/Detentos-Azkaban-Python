#Essa é a aplicação principal, aqui vão as funções principais para o programa funcionar
#importando as bibliotecas
import os

from modelos.azkaban import exibir_nome_do_programa, exibir_opcoes, escolher_opcao


def main(): #função main para inciar o programa numa certa ordem
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()