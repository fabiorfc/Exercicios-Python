# -*- coding: utf-8 -*-
"""
14 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa 
disciplina ao longo de um semestre, e calcule a sua média. A atribuição de 
conceitos obedece à tabela abaixo:
    * Média de Aproveitamento  Conceito
    * Entre 9.0 e 10.0        A
    * Entre 7.5 e 9.0         B
    * Entre 6.0 e 7.5         C
    * Entre 4.0 e 6.0         D
    * Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente 
e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o 
conceito for D ou E.
"""
nota_01 = float(input('Informe o valor da primeira nota: '))
nota_02 = float(input('Informe o valor da segunda nota: '))
#Atribuição e cálculo dos valores
media = (nota_01 + nota_02) / 2
if(media >= 9.0):
    conceito = 'A'
elif(7.5 <= media < 9):
    conceito = 'B'
elif(6.0 <= media < 7.5):
    conceito = 'C'
elif(4.0 <= media < 6.0):
    conceito = 'D'
else:
    conceito = 'E'
if(media >= 6.0):
    mensagem = 'APROVADO'
else:
    mensagem = 'REPROVADO'
#Impressão dos resultados
print('Notas dos alunos: {} e {}'.format(nota_01, nota_02))
print('Média do aluno: {}'.format(media))
print('Conceito: {}'.format(conceito))
print('Você foi: {}'.format(mensagem))