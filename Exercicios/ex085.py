'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

numeros = [[], []]


for c in range(0, 7):
    var = (int(input('Digite um valor: ')))

    if var % 2 == 0:
        numeros[0].append(var)
    else:
        numeros[1].append(var)

numeros[0].sort()
numeros[1].sort()
print(numeros)