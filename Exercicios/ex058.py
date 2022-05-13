'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
pc = randint(0, 10)
acertou = False
print(pc)

while not acertou:
    jogador = int(input('Digite um numero : '))
    if jogador == pc:
        acertou = True
    else:
        if jogador > pc:
            print('Voce errou, digite um valor menor!!')
        elif jogador < pc:
            print('Voce errou, digite um valor maior!!!')

print('Você venceuuu!!!')