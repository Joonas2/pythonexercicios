from Modulos.utilidades import moeda as m

valor = float(input('Digite o valor: '))

print(f'O dobro do valor {valor} é: {m.dobro(valor)}')
print(f'A metade do valor {valor} é: {m.metade(valor)}')
print(f'O aumento do valor {valor} em 10% é: {m.aumentar(valor, 10)}')
print(f'A diminuição do valor {valor} em 10% é: {m.diminuir(valor, 10)}')