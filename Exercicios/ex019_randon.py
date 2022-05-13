'''Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido. '''
from random import choice

a1 = str(input('Nome aluno um:  '))
a2 = str(input('Nome aluno dois: '))
a3 = str(input('Nome aluno três: '))
a4 = str(input('Nome aluno quatro: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)

print('O Aluno escolhido foi {}'.format(escolhido))