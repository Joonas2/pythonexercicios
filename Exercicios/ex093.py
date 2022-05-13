'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogador = dict()
golPartida = list()
total = 0

jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input('Quantas partidas ele jogou: '))

for partidas in range(0, jogador['partidas']):
    golPartida.append(int(input(f'Quantos gols ele fez na {partidas + 1}º partida: ')))

jogador['gols'] = golPartida[:] #recebendo uma lista no dicionario
jogador['total Gols'] = sum(golPartida) #somando o total de gols

print('-=' * 30)
print(jogador)

print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')

print('-=' * 30)
print(f'O Jogador {jogador["nome"]} jogou {jogador["partidas"]}')

for p, g in enumerate(golPartida):
    print(f'Na {p + 1}º ele fez {g}')
