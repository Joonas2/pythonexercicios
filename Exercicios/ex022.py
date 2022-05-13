'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:'''
nome = str(input('Digite seu nome completo: '))

print('\n01) O nome com todas as letras maiúsculas e minúsculas.')
print('Letras minusculas: ', nome.lower())
print('Letras maiusculas: ', nome.upper(), '\n')
#-----------------------------------------------------------------------------------------------------------------------
print('2) Quantas letras ao todo (sem considerar espaços).')
p = nome.replace(' ', '')
print('Total de letras:', len(p), '\n')


#-----------------------------------------------------------------------------------------------------------------------
print('3) Quantas letras tem o primeiro nome.')
primeiro = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(primeiro[0], len(primeiro[0])))