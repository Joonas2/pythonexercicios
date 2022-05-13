'''Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''
from math import cos, sin, tan, radians
ang = float(input('Digite o angulo: '))
seno = sin(radians(ang))
co = cos(radians(ang))
tang = tan(radians(ang))

print('O angulo {:.2f}º tem seno {:.2f}, cosseno {:.2f} e a tangente {:.2f} '.format(ang, seno, co, tang))
