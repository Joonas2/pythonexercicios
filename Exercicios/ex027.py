'''Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''
nome= str(input('Digite seu nome: ')).strip().lower()
n = nome.split()
print('Seu primeiro nome é {}'.format(n[0].title()))
print('Seu ultimo nome {}'.format(n[len(n)-1].title()))