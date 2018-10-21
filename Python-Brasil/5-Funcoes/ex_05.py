# -*- coding: utf-8 -*-
"""
5 - Faça um programa com uma função chamada somaImposto. A função possui dois 
parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas 
expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""
def soma_imposto(taxa_imposto, custo):
    
    #Conversão dos valores de int para float
    taxa_imposto = float(taxa_imposto)
    custo = float(custo)
    
    custo_total = custo * (1 + taxa_imposto/100)
    return(custo_total)
