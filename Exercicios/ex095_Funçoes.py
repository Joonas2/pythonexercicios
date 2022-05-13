'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''
def area(base, altura):
    a = base * altura
    print(f' A área do terreno é {a:.2f}')

base = float(input('Digite a base: '))
altura = float(input('Digite a altura :'))
area(base, altura)
