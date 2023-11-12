from app import *
from time import sleep as sl


def inicialização():
    while True:
        menu(['CriarArquivo', 'Nome', 'Idade', 'E-mail', 'Telefone', 'Cidade', 'Estado', 'AddClientes', 'Sair do sistema'])
        opcao = int(input('Digite Sua(as) opcoes: '))
        sl(1)
        while 0 < opcao > 9:
            opcao = int(input('Digite Sua(as) opcoes: '))
            print(' ')
            cabeçalho('\033[31m Opção inválida!\n \033[32m Digite um número de\033[31m [\033[33m1/9\033[31m]')
            sl(1)
            
        if opcao == 1:
            print(' ')
            cliente = criarArquivo()
            cabeçalho(cliente[0])
            sl(1)
            
        elif opcao == 2:
            print(' ')
            encontrarNome()
            sl(1)
            
        elif opcao == 3:
            print(' ')
            idade = idadePesquisa()
            cabeçalho(f'\033[36m A idade pesquisada é\033[34m {idade}')
            sl(1)
            
        elif opcao == 4:
            print('')
            emailPesquisado = EmailPesquisa()
            cabeçalho(f'\033[36m O email da pessoa pesquisada é\033[33m {emailPesquisado} ')
            sl(1)
            
        elif opcao == 5:
            print('')
            telefonePesquisado = TelefonePesquisa()
            cabeçalho(f'\033[36m O Telefone da pessoa pesquisada é\033[37m {telefonePesquisado} ')
            sl(1)
            
        elif opcao == 6:
            print('')
            cidadePesquisado = CidadePesquisa()
            cabeçalho(f'\033[36m A Cidade da pessoa pesquisada é\033[31m {cidadePesquisado} ')
            sl(1)
            
        elif opcao == 7:
            print('')
            EstadoPesquisado = EstadoPesquisa()
            cabeçalho(f'\033[36m O Estado da pessoa pesquisada é\033[32m {EstadoPesquisado} ')        
            sl(1)
            
        elif opcao == 8:
            print('')
            novoCliente = AddCliente()
            cabeçalho(f'\033[36m Informações e cadastro do cliente\033[33m {novoCliente[0]}\033[36m criado com sucesso')
            sl(1)
            
        elif opcao == 9:
            print('')
            cabeçalho('\033[31m Saindo do Sistema!')
            break    
            
    print('\033[32m Sistema Finalizado com Sucesso:')


    


