from Projeto.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #vai mandar abrir o arquivo
        a.close()
    except FileNotFoundError: #se o arquivo não existir vai dar erro, e retornar um false
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print('Houve um erro')
    else:
        print('Arquivo criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print('Erro ao ler arquivo')
    else:
        cabeçalho('Pessoas Cadastradas')
        print(a.read())


def adicionarPessoas(arquivo, nome, idade):
    try:
        a = open(arquivo, "at")
    except:
        print('Houve um erro')
    else:
        a.write(f'\n{nome}; {idade}')
    finally:
        a.close()