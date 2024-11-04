#Esse projeto funcionará basicamente como um programa para registrar detento de Azkaban (prisão de segurança maxima do universo de Harry Potter)
import os

class Detento: 
    def __init__(self, nome, numero, idade, sexo):
        self._nome = nome
        self._numero = numero
        self._idade = idade
        self._sexo = sexo

    def __str__(self):
        return f'{self._nome} - {self._numero} - {self._idade} - {self._sexo}'

class RegistroDeDetentos:
    def __init__(self):
        self.detentos = []

    def cadastrar_novo_detento(self): 
        exibir_subtitulo('Cadastro de um novo detento em Azkaban')

        nome = input('\nDigite o nome do detento: ').title() #coloque .title() para deixar a primeira letra do nome e do sobrenome maiusculas
        numero = int(input('Digite o número do detento: '))
        if numero < 1: #caso o numero seja menor que 1, o programa vai dizer que o numero invalidou e voltar ao menu sem salvar o cadastro
            print('Numero inválido')
            voltar_ao_menu_principal()
            return
        for detento in self.detentos: #caso o numero ja tenha sido usado, o programa vai dizer que o numero invalidou e voltar ao menu sem salvar o cadastro
            if detento._numero == numero:
                print('Numero já está sendo usado!')
                voltar_ao_menu_principal()
                return
        idade = int(input('Digite a idade do detento: '))
        sexo = input('Digite o sexo do detento (M/F): ').upper()
        if sexo not in ['M', 'F']: #caso isso ocorra, o programa vai dizer que o sexo invalidou e voltar ao menu sem salvar o cadastro
            print('Sexo inválido')
            voltar_ao_menu_principal()
            return
        detento = Detento(nome, numero, idade, sexo)
        self.detentos.append(detento)
        print(f'\nDetento {nome} cadastrado com sucesso!')
        voltar_ao_menu_principal()

    def listar_detentos(self):
        exibir_subtitulo('Lista de detentos de Azkaban')

        if not self.detentos:
            print('Nenhum detento cadastrado.')
        else:
            print(f'{'Nome do detento'.ljust(20)} | {'Numero do detento'.ljust(17)} | {'Idade do detento'.ljust(16)} | {'Sexo do detento'.ljust(10)}')
            for detento in self.detentos:
                #tive que transformar os atributos 'detento._numero' e o 'detento._idade' em str para poder aplicar o método .ljust()
                print(f'{detento._nome.ljust(20)} | {str(detento._numero).ljust(17)} | {str(detento._idade).ljust(16)} | {detento._sexo.ljust(10)}')
        voltar_ao_menu_principal()

    def atualizar_dados_de_um_detento(self):
        exibir_subtitulo('Atualizar dados de um detento')

        pesquisa = input('Digite o nome do detento que deseja atualizar: ').title()
        if not pesquisa: #caso nao tenha nada preenchido no campo, ele dirá 'nome invalido' e voltará para o menu principal
            print('Nome inválido')
            voltar_ao_menu_principal()
            return

        encontrou = False

        for detento in self.detentos: #serve para nao precisar pesquisar o nome completo do detento, agilizando a busca
            if detento._nome.find(pesquisa) != -1:
                encontrou = True
                detento_alterar = detento._nome
                break
        
        if encontrou: #caso o nome do detento seja encontrado
                print(f'\nDetento encontrado!')
                print(f'Nome: {detento._nome}')
                print(f'Numero: {detento._numero}')
                print(f'Idade: {detento._idade}')
                print(f'Sexo: {detento._sexo}')
                
                novo_nome = input('\nDigite o novo nome do detento: ').title()
                novo_numero = int(input('Digite o número do detento: '))
                if novo_numero != detento._numero:  # para verificar se o novo numero é diferente do atual
                    for outro_detento in self.detentos:
                        if outro_detento._numero == novo_numero:
                            print('Número já está sendo usado!')
                            voltar_ao_menu_principal()
                            return
                nova_idade = int(input('Digite a idade do detento: '))
                novo_sexo = input('Digite o sexo do detento (M/F): ').upper()
                if novo_sexo not in ['M', 'F']:
                    print('Sexo inválido')
                    voltar_ao_menu_principal()
                    return

                #Tive que armazenas as informações temporariamente para caso o usuário digitasse algo diferente de M ou F, não atualizar direto na lista (estava ocorrendo e ja estava prestes a arrancar os cabelos)
                detento._nome = novo_nome
                detento._numero = novo_numero
                detento._idade = nova_idade
                detento._sexo = novo_sexo

                print(f'\nDados do detento {detento_alterar} atualizados com sucesso!')
                voltar_ao_menu_principal()
        else:
            print('Detento não encontrado')
            voltar_ao_menu_principal()

    def excluir_detento(self):
        exibir_subtitulo('Excluir um detento')

        nome = input('Digite o nome do detento que deseja excluir: ').title()
        for detento in self.detentos:
            if detento._nome == nome:
                pergunta = input(f'Tem certeza que deseja excluir o detento {nome}? (S/N): ')
                if pergunta.upper() == 'S':
                    self.detentos.remove(detento) #usei o .remove para remover pelo nome em vez do indice
                    print(f'\nDetento {nome} excluído com sucesso!')
                else:
                    print('Exclusão cancelada')
                voltar_ao_menu_principal()
        print('Detento não encontrado')
        voltar_ao_menu_principal()

    def finalizar_app(self): #função caso a pessoa queira sair do programa 
        limpar_tela()
        print('Finalizando app')
        exit()

    def opcao_invalida(self):
        print('\nOpção inválida, tente novamente.')
        voltar_ao_menu_principal()

def exibir_nome_do_programa(): #função para exibir o nome do programa
    print('''
--------------------------------------------------


        ʀᴇɢɪᴤᴛʀᴏ ᴅᴇ ᴅᴇᴛᴇɴᴛᴏᴤ ᴅᴇ ᴀᴢᴋᴀʙᴀɴ


--------------------------------------------------
''')

def exibir_subtitulo(texto): #vi que estava sempre usando um subtitulo quando escolhia uma opção entao decidir tranformar em função
    limpar_tela()
    linha = '-' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear') #serve para limpar o console seja o sistema operacional windows ou linux

def exibir_opcoes(): #essa função vai exibir as opções para o usuario selecionar
    print('1. Cadastrar novo detento')
    print('2. Listar detentos')
    print('3. Atualizar dados de um detento')
    print('4. Excluir detento')
    print('5. Sair')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))#estava pensando em colocar a lista de detentos para aparecer quando o usuário quiser atualizar dados de um detento e quando quiser excluior detento
        if opcao_escolhida == 1:
            limpar_tela()
            registro.cadastrar_novo_detento()#deve mostrar para cadastrar o detento incluindo nome, número do detento, idade e sexo
        elif opcao_escolhida == 2:
            limpar_tela()
            registro.listar_detentos()#deve mostrar todos os detentos cadastrados numa lista com nome, número, idade e sexo 
        elif opcao_escolhida == 3:
            limpar_tela()
            registro.atualizar_dados_de_um_detento()#deve perguntar ao usuarios qual detento deseja modificar e qual dos itens quer modificar
        elif opcao_escolhida == 4:
            limpar_tela()
            registro.excluir_detento()#deve perguntar ao usuário qual detento deseja excluir e após selecionar o usuário, aparecer "deseja mesmo excluir detento <nome do detento>"
        elif opcao_escolhida == 5:
            limpar_tela()
            registro.finalizar_app()
        else:
            registro.opcao_invalida()
    except ValueError:
        registro.opcao_invalida()

def voltar_ao_menu_principal(): #função para retornar ao menu
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def main(): #função main para inciar o programa numa certa ordem
    limpar_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

registro = RegistroDeDetentos() #decidir criar registro global para nao ficar repetindo 

#Comentario: Eu fiz esse mesmo programa sem aplicar orientação a objetos e esse orientado a objetos e foi o que mais me fez passar noites mal dormidas...
