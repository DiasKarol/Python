""" Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário (se nota maior que 7 aprovado se não reprovado). No final, mostre o conteúdo gravado no dicionário.  """

aluno = {}

aluno['nome'] = input('Insira o nome do aluno: ')
aluno['media'] = float(input('Insira a média do aluno: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

print(aluno)