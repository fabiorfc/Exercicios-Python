# -*- coding: utf-8 -*-
"""
12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo 
que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
altura = float(input('Informe sua altura, em metros: '))
peso_ideal = 72.7 * altura - 58
print('Sua altura ideal é de: {}kg'.format(peso_ideal))