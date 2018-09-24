# -*- coding: utf-8 -*-
"""
15 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá 
informar se os valores podem ser um triângulo. Indique, caso os lados formem 
um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    Dicas:
    * Três lados formam um triângulo quando a soma de quaisquer dois lados for 
    maior que o terceiro;
    * Triângulo Equilátero: três lados iguais;
    * Triângulo Isósceles: quaisquer dois lados iguais;
    * Triângulo Escaleno: três lados diferentes;
"""
print('Informe os três lados de um triângulo')
lado_a = float(input('Informe o valor do comprimento do primeiro lado: '))
lado_b = float(input('Informe o valor do comprimento do segundo lado: '))
lado_c = float(input('Informe o valor do comprimento do terceiro lado: '))
#Validando a dica 1
if((lado_a + lado_b < lado_c) or (lado_c + lado_a < lado_b) or (lado_b + lado_c < lado_a)):
    print('As dimensões informadas não forma um triângulo')
else:
    #Triângulo equilátero
    if(lado_a == lado_b == lado_c):
        print('O triângulo é equilátero')
    #Triângulo isósceles
    elif(lado_a == lado_b):
        if((lado_a != lado_c) and (lado_b != lado_c)):
            print('O triângulo é isósceles')
    elif(lado_b == lado_c):
        if((lado_b != lado_a) and (lado_c != lado_a)):
            print('O triângulo é isósceles')
    elif(lado_a == lado_c):
        if((lado_a != lado_b) and (lado_c != lado_b)):
            print('O triângulo é isósceles')
    #Triângulo escaleno
    elif((lado_a != lado_b) and (lado_b != lado_c) and (lado_c != lado_a)):
        print('O triângulo é escaleno')