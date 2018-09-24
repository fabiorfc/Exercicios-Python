# -*- coding: utf-8 -*-
"""
13 - Faça um Programa que leia um número e exiba o dia correspondente da 
semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer 
valor inválido.
"""
numero = int(input('Informe um valor numérico: '))
if(numero == 1):
    dia_semana = 'Domingo'
    print(dia_semana)
elif(numero == 2):
    dia_semana = 'Segunda'
    print(dia_semana)
elif(numero == 3):
    dia_semana = 'Terça'
    print(dia_semana)
elif(numero == 4):
    dia_semana = 'Quarta'
    print(dia_semana)
elif(numero == 5):
    dia_semana = 'Quinta'
    print(dia_semana)
elif(numero == 6):
    dia_semana = 'Sexta'
    print(dia_semana)
elif(numero == 7):
    dia_semana = 'Sábado'
    print(dia_semana)
else:
    print('Valor inválido')
