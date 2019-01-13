# -*- coding: utf-8 -*-
"""
    5. Nome na vertical em escada invertida. Altere o programa anterior de 
modo que a escada seja invertida.
    FULANO
    FULAN
    FULA
    FUL
    FU
    F
"""
def nome_na_vertical_02():
   
    nome = input('Digite seu nome: ')
    nome = nome.upper()
    
    for i in range(len(nome), -1, -1):
        print(nome[:i])
