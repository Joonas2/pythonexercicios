'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

valores = []
par = []
impar = []

while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar [S/N] ? ')).lower()
    if continuar not in 'sn':
        continuar = str(input('Invalido. Deseja continuar [S/N]? '))
    elif continuar in 'n':
        break
for numero in valores:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(f'Original = {valores}')
print(f'Par: {par}')
print(f'Impar {impar}')
