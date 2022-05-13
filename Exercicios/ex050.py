'''Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''
s = 0

for c in range(0, 6):
    valor = int(input('Digite o {} valor: '.format(c)))
    if valor % 2 == 0:
        s = s + valor

print(s)



