# -*- coding: utf-8 -*-
"""
14 - Faça um programa que peça 10 números inteiros, calcule e mostre a 
quantidade de números pares e a quantidade de números impares.
"""
#Declarando os objetos
numeros = []
impares, pares = 0, 0

#Coletando os dados e calculando os resultados
print('\n Digite 10 números')
for x in range(1,11):
    numero = int(input('{}° numero: '.format(x)))
    numeros.append(numero)

    #Calculando os resultados
    if(numero%2 == 0):
        pares += 1
    else:
        impares += 1

#Gerando os resultados
print('\n Dos números digitados, existem {} pares e {} ímpares'.format(pares, impares))