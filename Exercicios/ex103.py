''''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
 Ex: n = leiaInt(‘Digite um n: ‘)'''

def leiaInt(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = n
            ok = True
        else:
            print('Erro ! Valor invalido')

        if ok:
            break

    return valor

n = leiaInt('Digite um numero: ')
print(f'Valor foi {n}')



