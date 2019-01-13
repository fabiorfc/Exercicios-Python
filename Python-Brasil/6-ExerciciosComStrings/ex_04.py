# -*- coding: utf-8 -*-
"""
    4 - Nome na vertical em escada. Modifique o programa anterior de forma a 
mostrar o nome em formato de escada.

        F
        FU
        FUL
        FULA
        FULAN
        FULANO
"""
def nome_na_vertical():
    
    nome = input('Digite seu nome: ')
    nome = nome.upper()
    
    for i in range(0, len(nome)+1):
        print(nome[:i])



