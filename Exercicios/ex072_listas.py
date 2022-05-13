'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze','treze',
'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


#Validação do numero digitado pelo usuario
while True:
    usuario = int(input('Digite um numero de 0 a 20: '))
    if 0 <= usuario <= 20: #Usuario >=  0 e  usuario < = 20
             break
    print('Invalido, digite novamente')
#-----------------------------------------------------------------------

print(f'Você digitou o numero {numero[  usuario]}')
