# -*- coding: utf-8 -*-
"""
13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um 
algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    a) Para homens: (72.7*h) - 58
    b) Para mulheres: (62.1*h) - 44.7
"""
altura = float(input('Informe sua altura, em metros: '))
peso_ideal_m = round(72.7 * altura - 58, 1)
peso_ideal_f = round(62.1 * altura - 44.7, 1)
print('Sua altura ideal é de:')
print(' {}kg, caso seja do sexo Masculino'.format(peso_ideal_m))
print(' {}kg, caso seja do sexo Feminino'.format(peso_ideal_f))