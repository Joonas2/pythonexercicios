'''Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.'''
nome = str(input('Digite o nome da cidade: ')).lower().strip()
n = nome.split()
print('santo' in n[0])