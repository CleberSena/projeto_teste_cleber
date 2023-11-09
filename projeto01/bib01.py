import os

def linha(tam=50):
    return '\033[1;32m-' * tam

def cabecalho(txt):    
    print(txt.center(55))
    print(linha())

def menu(lista):
    cabecalho('\033[1;33mMenu Principal')
    c = 0
    for item in lista:
        print(f'\033[1;35m{c}\033[32m =>\033[35m {item}')
        c += 1

def informacoesPessoais():
    nome = input('Digite seu nome: ').strip().upper()
    email = input('Digite seu email: ').strip()
    telefone = int(input('Digite seu Contato de Telefone com DDD: '))
    Cidade = input('Digite sua Cidade: ').strip().upper()
    Estado = input('Digite seu Estado: ').strip().upper()
    return nome, email, telefone, Cidade, Estado



class dadosPessoais:
    def __init__(self, nome, email, telefone, Cidade, Estado):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.Cidade = Cidade
        self.Estado = Estado
        Sair_Do_Sistema = '\033[31mFinalizando o Sistema! Volte swmpre:'