from bib01 import cabecalho
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31m Houve ERRO! Na criação do arquivo:')
    else:
        print(f'\033[36m Arquivo\033[33m {nome}\033[36m criado com susseço')

def lerArquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabecalho('Pessoas cadastradas')
        print(a.read())
    finally:
        a.close()

def Cadastrar(arq, nome, email, telefone, Cidade, Estado):
    try:
        a = open(nome, email, telefone, Cidade, Estado, 'at')
    except:
        print('\033[31m Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}\n'
                      '{email}\n'
                      '{telefone}\n'
                      '{Cidade}\n'
                      '{Estado}\n')
        except: 
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome, email, telefone, Cidade, Estado} adicionado')
            a.close()

    