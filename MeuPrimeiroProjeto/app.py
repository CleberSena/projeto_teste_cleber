def linha(tam = 50):
    return '-' * tam

def cabeçalho(txt):
    print(txt.center(55))
    print(linha())

def menu(name):
    c = 1
    for iten in name:
        print(f'\033[31m[\033[33m{c}\033[31m]\033[34m=>\033[36m {iten}')
        c += 1

def criarArquivo():
    PytonistaAutodidata = []
    nome = input('digite seu nome')
    PytonistaAutodidata.append(nome)
    idade = input('digite sua idade') 
    PytonistaAutodidata.append(idade)
    email = input('digite seu Email') 
    PytonistaAutodidata.append(email)
    telefone = input('digite seu telefone') 
    PytonistaAutodidata.append(telefone)
    cidade = input('digite sua Cidade') 
    PytonistaAutodidata.append(cidade)
    estado = input('digite seu Estado') 
    PytonistaAutodidata.append(estado)
    with open('PytonistaAutodidata.txt', 'w',encoding='utf-8') as arquivo:
        for iten in PytonistaAutodidata:
            arquivo.write(str(iten) + '\n')
    return PytonistaAutodidata

def AddCliente():
    PytonistaAutodidata = []
    nome = input('digite seu nome')
    PytonistaAutodidata.append(nome)
    idade = input('digite sua idade') 
    PytonistaAutodidata.append(idade)
    email = input('digite seu Email') 
    PytonistaAutodidata.append(email)
    telefone = input('digite seu telefone') 
    PytonistaAutodidata.append(telefone)
    cidade = input('digite sua Cidade') 
    PytonistaAutodidata.append(cidade)
    estado = input('digite seu Estado') 
    PytonistaAutodidata.append(estado)
    with open('PytonistaAutodidata.txt', 'a',encoding='utf-8') as arquivo:
        for iten in PytonistaAutodidata:
            arquivo.write(str(iten) + '\n')
    return PytonistaAutodidata

def lerArquivo():
    with open('PytonistaAutodidata.txt', 'r',encoding='utf-8') as arquivo:
        mensag = arquivo.readlines()
        return mensag
       
def encontrarNome():
    while True:
        cont = lerArquivo()
        pes = input('qual é o seu nome: ')
        for iten in cont:
            if pes in iten:
                print(f'\033[36m O nome pesquisado foi o de\033[32m {iten}' )
        break
    
def encontrarIdade():
    while True:
        cont = lerArquivo()
        pes = input('pesquisar idade de quem? ')       
        for c, iten in enumerate(cont):            
            if pes in iten:
                return c
def idadePesquisa():
    pesq = encontrarIdade()
    c = pesq + 1
    dado = lerArquivo()
    return dado[c]

def encontrarEmail():
    while True:
        cont = lerArquivo()
        pes = input('pesquisar Email de quem? ')       
        for c, iten in enumerate(cont):            
            if pes in iten:
                return c
def EmailPesquisa():
    pesq = encontrarEmail()
    c = pesq + 2
    dado = lerArquivo()
    return dado[c]

def encontrarTelefone():
    while True:
        cont = lerArquivo()
        pes = input('Pesquisar Telefone de quem? ')       
        for c, iten in enumerate(cont):            
            if pes in iten:
                return c
def TelefonePesquisa():
    pesq = encontrarTelefone()
    c = pesq + 3
    dado = lerArquivo()
    return dado[c]

def encontrarCidade():
    while True:
        cont = lerArquivo()
        pes = input('Pesquisar Cidade de quem? ')       
        for c, iten in enumerate(cont):            
            if pes in iten:
                return c
def CidadePesquisa():
    pesq = encontrarCidade()
    c = pesq + 4
    dado = lerArquivo()
    return dado[c]

def encontrarEstado():
    while True:
        cont = lerArquivo()
        pes = input('Pesquisar Estado de quem? ')       
        for c, iten in enumerate(cont):            
            if pes in iten:
                return c
def EstadoPesquisa():
    pesq = encontrarEstado()
    c = pesq + 5
    dado = lerArquivo()
    return dado[c]