'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter
ranking = list()

jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6),
        'jogador 5': randint(1, 6),
        'jogador 6': randint(1, 6),
}

for k, v in jogo.items():
    print(f'O {k} tirou o valor {v}')
    sleep(1)
print('-=-'* 20)

ranking = sorted(jogo.items(), key= itemgetter(1), reverse=True)
#sorted irá organizar os items, utilizando a chave do itemgetter(1), que significa: 1 ira pegar o valor de randint, 0 o valor de jogador
print(ranking) #ranking sera um lista, mesmo que eu o defina como dicionario

for p, j in enumerate(ranking):
    print(f'O {p + 1}º foi o {j[0]} com valor {j[1]}')
