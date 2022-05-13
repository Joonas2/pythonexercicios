'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
idade = (date.today().year) - ano
quartel = ano + 18

if idade < 18:
    print('Você tem {} anos e ainda não se alistou'.format(idade))
    print('Voce ira se alistar no ano de {}'.format(quartel))
elif idade == 18:
    print('Voce ira se alistar esse ano, pois tem {}'.format(idade))

else:
    print('Você tem {} e se alistou no ano de {}'.format(idade, quartel))