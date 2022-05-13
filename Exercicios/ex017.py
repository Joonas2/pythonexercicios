'''Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa. '''
import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hipo = math.sqrt((math.pow(co, 2)) + (math.pow(ca, 2)))
print('Hipotenusa do triangulo é {:.2f}'.format(hipo))
