'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar [S/N]? ')).lower()

    if continuar not in 'sn':#Validação para continuar
        continuar = str(input('Argumento invalido. Deseja continuar [S/N]? ')).lower()
    elif continuar in 'n':
        break

print(f'Você digitou {len(valores)}')
valores.sort(reverse=True)
print(f'A forma decrescente dos valores são: {valores}')

if 5 in valores:
    print('O valor 5 está na lista')
else:
    print(f'O valor 5 não está na lista ')

