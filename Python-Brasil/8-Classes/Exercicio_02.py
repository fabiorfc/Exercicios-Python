#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classe Quadrado: Crie uma classe que modele um quadrado:
    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado:
    
    def __init__(self, lado):
        self.lado = lado
    
    def Get_lado(self):
        return self.lado

    def AreaQuadrado(self):
        return self.lado*self.lado


# Tipos de quadrado
quadrado_01 = Quadrado(5)
quadrado_02 = Quadrado(10)


# Verificando o valor do lado
print("O valor do lado é: {}".format(quadrado_01.Get_lado()))
print("O valor do lado é: {}".format(quadrado_02.Get_lado()))


# Verificando a área do quadrado
print("O valor da área é: {}".format(quadrado_01.AreaQuadrado()))
print("O valor da área é: {}".format(quadrado_02.AreaQuadrado()))



