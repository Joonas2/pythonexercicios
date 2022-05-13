'''Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''
import urllib
import urllib.request

try:
    pagina = urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('Pagina fora do ar')
else:
    print('Tudo ok')
