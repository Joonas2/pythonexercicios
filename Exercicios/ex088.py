'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
jogos = list()
listaNumeros = list()


quantidadeJogos = int(input('Quantos jogos deseja gerar ?: '))

for geradorJogos in range(0, quantidadeJogos):
    for geradorNumeros in range(0, 6):
      numeros = randint(1, 60)
      listaNumeros.append(numeros)

    jogos.append(listaNumeros[:])
    listaNumeros.clear()


for i in range(0, quantidadeJogos):
    print(f'A {i+1} cartela ficou com os numeros: {jogos[i]}')

