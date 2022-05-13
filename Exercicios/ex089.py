'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
from statistics import mean
dados = list()
alunos = list()



while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota um: ')))
    dados.append(float(input('Nota dois: ')))

    media = mean(dados[1:])
    dados.append(media)

    alunos.append(dados[:])
    dados.clear()
    continuarCad = str(input('Deseja continuar [S/N]: ')).lower()
    if continuarCad == 'n':
        break
    print('-=-' * 20)



while True:
    print('Nº Nome     Media')
    for pos, var in enumerate(alunos):
        print(f'{pos} {var[0]:>4} {var[3]:>8}')

    print('-=-'* 20)

    while True:
        visualizar = int(input('Digite o nº para ver as notas ou 999 para sair: '))
        if visualizar == 999:
            break
        else:
            print('Nº Nota 1    Nota 2')
            for pos, var in enumerate(alunos):
                print(f'{pos[visualizar]} {var[1]:>5} {var[2]:>9}')
    print('-=-' * 20)


