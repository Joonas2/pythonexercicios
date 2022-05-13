'''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'''
import time
import random
var = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

print('-=-'*30)
print(' '*25, 'BEM VINDO AO JOGO DE JOKENPÔ')
print('-=-'*30, '\n')
time.sleep(3)

print('[0] Pedra'
      '[1] Papel'
      '[2] Tesoura')
jogador = int(input('Escolha uma opção: '))

#--------------------------------------------------------------------
print('-=-'*30)
print(' '*30, 'CARREGANDO...')
print('-=-'*30, '\n')
time.sleep(3)
#---------------------------------------------------------------------

print('Você escolheu {} e o computador escolheu {}'.format(var[jogador], var[computador]))

if jogador == 0 and computador == 2:
    print('Voce venceu')
elif jogador == 0 and computador == 1:
    print('Você perdeu')
elif jogador == 0 and computador == 0:
    print('Empate')

#------------------------------------------------------
#PAPEL
elif jogador == 1 and computador == 0:
    print('Voce venceu')
elif jogador == 1 and computador == 2:
    print('Você perdeu')
elif jogador == 1 and computador == 1:
    print('Empate')

#------------------------------------------------------
#tesoura
elif jogador == 2 and computador == 1:
    print('Voce venceu')
elif jogador == 2 and computador == 0:
    print('Você perdeu')
elif jogador == 2 and computador == 2:
    print('Empate')