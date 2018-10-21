# -*- coding: utf-8 -*-
"""
12 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer 
número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja 
ver a tabuada. A saída deve ser conforme o exemplo abaixo:
    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50
"""
#Coletando os dados
numero = int(input('Informe o número que deseja ver a tabuada: '))

#Gerando os resultados
print('TAbuada do {}'.format(numero))
for x in range(0, 11):
    print('{} X {} = {}'.format(numero, x, numero*x))