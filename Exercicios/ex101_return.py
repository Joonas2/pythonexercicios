'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
 retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''
from datetime import date
hoje = date.today().year


def voto(nascimento):
    idade = hoje - nascimento
    if 15 < idade < 18 and idade > 65:
        return f'Voce tem  {idade} anos. Voto Opcional'
    elif 18 < idade < 65:
        return f'Voce tem  {idade} anos.Voto obrigatorio'
    else:
        return f'Voce tem  {idade} anos.Voto negado'

teste = int(input('Digite seu ano de nascimento: '))
print(voto(teste))