# -*- coding: utf-8 -*-
"""
15 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""
#Input dos dados
n = int(input('Insira o valor limite n: '))
serie_x1 = 0
serie_x2 = 1

#Cálculos
print(serie_x2)
for x in range(0, n-1):
    resultado = serie_x1 + serie_x2
    serie_x1 = serie_x2
    serie_x2 = resultado
    
    print(resultado)
    

