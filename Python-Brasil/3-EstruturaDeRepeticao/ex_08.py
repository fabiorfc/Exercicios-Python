# -*- coding: utf-8 -*-
"""
8 - Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
numeros = []
for x in range(1,6):
    numero = float(input('\n Digite o {}° número: '.format(x)))
    #Certificação dos números de tipo numérico
    numeros.append(numero)
    
#Efetuando os cálculos
soma = sum(numeros)
media = soma/len(numeros)

#Gerando os resultados
print('\n A soma dos valores e a média dos valores são: {} e {} respc.'.format(soma, media))