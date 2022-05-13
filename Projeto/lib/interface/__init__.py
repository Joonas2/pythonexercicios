def linha(tam=42):
    return '=' * tam

def cabeçalho(txt):
    print(linha())
    print(f'{txt.center(42)}')
    print(linha())

def menu(lista):
    cabeçalho('Menu')
    for itens in lista:
        print(f'{itens} ')
    print(linha())
    opção = leiaInteiro('Sua opção: ')

    return opção

def leiaInteiro(valor):
    while True:
        try:
            numero = int(input(valor))
        except(ValueError, TypeError) :
            print('Digite um valor valido')
            continue
        except (KeyboardInterrupt):
            print('O usuario não digitou nada')
            return 0
        else:
            return numero

