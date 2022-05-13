'''Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''
from Modulos.utilidades import moeda as m


valor = float(input('Digite o valor: '))

print(f'O dobro do valor {m.moeda(valor)} é {m.dobro(valor, True)}')#True esta sendo passado para parametro Formatar
print(f'A metade do valor {m.moeda(valor)} é {m.metade(valor, True)}')
print(f'O aumento do valor {m.moeda(valor)} em 10% é {m.aumentar(valor, 10, True)}')
print(f'A diminuição do valor {m.moeda(valor)} em 10% é {m.diminuir(valor, 10, True)}')