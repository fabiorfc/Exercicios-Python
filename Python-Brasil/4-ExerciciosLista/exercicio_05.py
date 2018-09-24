# -*- coding: utf-8 -*-
"""
5) Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.
"""
def exercicio_05(vetor):
    #Declarando os vetores que serão utilizados
    par = []
    impar = []
    numeros = [1,2,3,4,5,6,7,8]
    #Loop para identificar os pares e impares
    for i in range(0, len(numeros)):
        if numeros[i]%2 == 0:
            par.append(numeros[i])
        else:
            impar.append(numeros[i])
    #Escrevendo os resultados
    print('Vetor divulgados: {}'.format(numeros))
    print('Vetor de números pares: {}'.format(par))
    print('Vetor de números ímpares: {}'.format(impar))