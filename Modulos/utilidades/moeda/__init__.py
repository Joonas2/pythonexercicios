def aumentar(valor=0, taxa=0, formatar=False):
    res = valor * (1 + (taxa/100))
    return res if formatar is False else moeda(res)
#retornar o res se formatar for falso, isto é, ira retornar o valor sem formatação da função moeda(), senão retorno o res formatado com a fução moeda


def diminuir(valor=0, taxa=0, formatar=False):
    res = valor * (1 - (taxa/100))
    return res if not formatar else moeda(res)
#retornar o res se não for para formatar, senão formatar ela com a função moeda()

def dobro(valor=0, formatar=False):
    res = valor * 2
    return res if not formatar else moeda(res)


def metade(valor=0, formatar=False):
    res = valor / 2
    return res if not formatar else moeda(res)

def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, aumento = 0, desconto=0):

     print('-='* 20)
     print(f'Analisando o valor {moeda(valor)}\n'
            f'O dobro: \t{dobro(valor, True)}\n'
            f'A metade: \t{metade(valor, True)}\n'
            f'O Aumento: \t{aumentar(valor, aumento, True)}\n'
            f'O Desconto:\t{diminuir(valor, desconto, True)} \n')
