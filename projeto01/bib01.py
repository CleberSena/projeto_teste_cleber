def linha(tam=50):
    return '\033[1;32m-' * tam

def cabecalho(txt):    
    print(txt.center(55))
    print(linha())

def menu(lista):
    cabecalho('\033[1;33mMenu Principal')
    c = 1
    for item in lista:
        print(f'\033[1;35m{c}\033[32m =>\033[35m {item}')
        c += 1

class dadosPessoais:
    def __init__(self):
        self.nome = "\033[36mCleber Winkestroter Sena"
        self.email = "\033[37mkalebydev@hgmail.com"
        self.telefone = "\033[34m(33)-987040542"
        self.Cidade = "\033[33mJoão Molevade"
        self.Estado = "\033[32mMinas Gerais"