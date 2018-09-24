# -*- coding: utf-8 -*-
"""
5 - Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
    - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    - A mensagem "Reprovado", se a média for menor do que sete;
    - A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
nota_01 = float(input('Digite o valor da primeira nota: '))
nota_02 = float(input('Digite o valor da segunda nota: '))
media = (nota_01 + nota_02) / 2
if( media == 10 ):
    print('Aprovado com Distinção')
elif( media >= 7.0):
    print('Aprovado')
else:
    print('Reprovado')