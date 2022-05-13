'''Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

alunos = dict()
alunos['nome'] = str(input('Digite seu nome: '))
alunos['media'] = float(input('Digite a media: '))

if alunos['media'] >= 7:
    alunos['situaçao'] = 'aprovado'
elif 7 > alunos['media'] >= 5:
    alunos['situaçao'] = 'Recuperação'
else:
    alunos['situaçao'] = 'reprovado'

print('-=' * 20)
for k, v in alunos.items():
    print(f'{k}: {v}')

