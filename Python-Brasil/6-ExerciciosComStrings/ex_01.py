# -*- coding: utf-8 -*-
"""
1 - Tamanho de strings. Faça um programa que leia 2 strings e informe o 
conteúdo delas seguido do seu comprimento. Informe também se as duas strings 
possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
    Compara duas strings
    String 1: Brasil Hexa 2006
    String 2: Brasil! Hexa 2006!
    Tamanho de "Brasil Hexa 2006": 16 caracteres
    Tamanho de "Brasil! Hexa 2006!": 18 caracteres
    As duas strings são de tamanhos diferentes.
    As duas strings possuem conteúdo diferente.
"""


def strings(string_01, string_02):

    #Imprimindo o conteúdo e a sua dimensão
    print('\n Tamanho de "{}": {} caracteres'.format(string_01, len(string_01)))
    print('\n Tamanho de "{}": {} caracteres'.format(string_02, len(string_02)))
    
    #Verificando se os comprimentos são iguais
    if(len(string_01) == len(string_02)):
        print('\n As string possuem o mesmo comprimento')
    else:
        print('\n As string possuem comprimentos distintos')
    
    #Verficicando se as strings possuem o mesmo conteúdo
    if(string_01 == string_02):
        print('\n As string possuem o mesmo conteúdo')
    else:
        print('\n As string possuem conteúdos distintos')
    