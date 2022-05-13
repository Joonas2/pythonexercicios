'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
maior = 0
velho = ''
mulheres = 0
a = 0


for i in range(0, 4):
    nome = str(input('Digite seu nome completo: ')).strip().upper()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo M ou F: ')).strip().upper()
    a += + idade #ira fazer a soma de todas as idades e depois ira dividir fazendo a media
    print('-=-'*20)

    if sexo == 'M' and idade > maior:
        maior = idade
        velho = nome
    elif sexo == 'F' and idade < 20:
        mulheres += +1

media = a / 2

print('Mais velho {}'.format(velho))
print('Há {} mulheres com idade inferior a 20 anos'.format(mulheres))
print('A media de idade é {}'.format(media))