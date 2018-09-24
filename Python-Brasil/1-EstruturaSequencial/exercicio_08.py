# -*- coding: utf-8 -*-
"""
8 - Faça um Programa que pergunte quanto você ganha por hora e o número de 
horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido 
mês.
"""
valor_hora = float(input('Informe o valor da hora trabalhada: '))
total_horas = float(input('Informe o total de horas trabalhada no mês: '))
salario = valor_hora * total_horas
print('O sálario mensal é de: {}'.format(salario))