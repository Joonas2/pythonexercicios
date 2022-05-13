'''Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''

from random import randint as r
computador = r(0, 10)
vitorias = sair = 0
jogador = ' '

while True:

    while jogador not in 'PI': #Validação de par ou impar
          jogador = str(input('Digite [P] par ou [I] impar: ')).upper()

#------------------------------------------------------
    numero = int(input('Digite um numero: '))
    soma = numero + computador

#------------------------------------------------------
    if jogador == 'P' and soma % 2 == 0:
        vitorias = vitorias + 1
        print(f'Voce ganhou pois a soma de {numero} e {computador} é Par')

    elif jogador == 'P' and soma % 2 != 0:
        print(f'Você perdeu, pois a soma {numero} e {computador} é impar')
        break

#---------------------------------------------------------
    if jogador == 'I' and soma % 2 != 0:
        vitorias = vitorias + 1
        print(f'Voce ganhou pois a soma de {numero} e {computador} é impar')
    elif jogador == 'I' and soma % 2 == 0:
        print(f'Voce perdeu, pois a soma de {numero} e {computador} é par')
        break

print(f'\nVoce teve {vitorias} vitorias seguidas')
