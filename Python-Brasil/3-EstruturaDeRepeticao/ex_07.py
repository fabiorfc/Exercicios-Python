# -*- coding: utf-8 -*-
"""
7 - Faça um programa que leia 5 números e informe o maior número.
"""
#Inserção dos dados
numeros = []
for x in range(1,6):
    numero = float(input('\n Digite o {}° número: '.format(x)))
    #Certificação dos números de tipo numérico
    numeros.append(numero)

#Ordenando os números
for cont in range(4, -1, -1):
    for x in range(0, cont):        
        if(numeros[x]<numeros[x+1]):
            temp = numeros[x]
            numeros[x] = numeros[x+1]
            numeros[x+1] = temp

#Gerando os resultados
print('O maior número da lista é: {}'.format(numeros[0]))