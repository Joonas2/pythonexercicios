from Projeto.lib.interface import *
from Projeto.lib.arquivo import *
arquivo = 'curso.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)


while True:
    resposta = menu(['01 - Ver Pessoas', '02 - Adicionar pessoas', '03 - Sair'])

    if resposta == 1:
        cabeçalho('Opção 01 - Ver Pessoas')
        lerArquivo(arquivo)
    elif resposta == 2:
        cabeçalho('Opção 02 - Adicionar pessoas')
        nome = str(input('Nome: ')).strip()
        idade = int(input('Idade: '))
        adicionarPessoas(arquivo, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo...')
        break
    else:
        cabeçalho('Digite uma opção valida.')