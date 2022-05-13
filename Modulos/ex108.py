'''Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.'''
from Modulos.utilidades import moeda as m

valor = float(input('Digite o valor: '))

print(f'O dobro do valor {m.moeda(valor)} é {m.moeda(m.dobro(valor))}')
print(f'A metade do valor {m.moeda(valor)} é {m.moeda(m.metade(valor))}')
print(f'O aumento do valor {m.moeda(valor)} em 10% é {m.moeda(m.aumentar(valor, 10))}')
print(f'A diminuição do valor {m.moeda(valor)} em 10% é {m.moeda(m.diminuir(valor, 10))}')