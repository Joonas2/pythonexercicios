'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Digite seu sexo M/F: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Valor invalido, digite seu sexo M/F: ')).strip().upper()
print('Cadastro realizado com sucesso, seu sexo é {}'.format(sexo))





"""while c != 0:
    sexo = str(input('Digite seu sexo M/F: ')).upper()

    if sexo == 'M' or sexo == 'F':
       c = 0
    else:
        print('Valor invalido')

print('Seu sexo é {}'.format(sexo))"""


