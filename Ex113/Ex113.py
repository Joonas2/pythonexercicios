'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInteiro(valor):
    while True:
        try:
            numero = int(input(valor))
        except(ValueError, TypeError) :
            print('Digite um valor valido')
            continue
        except(KeyboardInterrupt):
            print('O usuario não digitou nada')
            return 0
        else:
            return numero


def leiaFloat(valor):
    while True:
        try:
            numero = float(input(valor))
        except(ValueError, TypeError) :
            print('Valor invalido')
            continue
        except(KeyboardInterrupt):
            print('Não foi digitado nada')
            return 0
        else:
            return numero

valorInt = leiaInteiro('Digite um numero inteiro: ')
print(valorInt)

valorFloat = leiaFloat('Digite um numero real')
print(valorFloat)
