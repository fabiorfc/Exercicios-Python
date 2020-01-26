#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classe Retangulo: Crie uma classe que modele um retangulo:

    Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, 
    a escolher)
    
    Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área 
    e calcular Perímetro;
    
    Crie um programa que utilize esta classe. Ele deve pedir ao usuário que
    informe as medidades de um local. Depois, deve criar um objeto com as 
    medidas e calcular a quantidade de pisos e de rodapés necessárias para
    o local.//
"""

class retangulo:
    
    def __init__(self, lado_A, lado_B):
        self.lado_A = float(lado_A)
        self.lado_B = float(lado_B)
        
    def Get_lado_A(self):
        return self.lado_A

    def Get_lado_B(self):
        return self.lado_B

    def Set_lado_A(self, lado):
        self.lado_A = lado

    def Set_lado_B(self, lado):
        self.lado_B = lado
        
    def Calcula_area(self):
        return self.lado_A * self.lado_B

    def Calcula_perimetro(self):
        return 2 * self.lado_A + 2 * self.lado_B
    
    

# Criando os valores dos retângulos
#retangulo_01 = retangulo(lado_A = 3, lado_B = 5)
#retangulo_02 = retangulo(lado_A = 4, lado_B = 4)


# Retornando os valores dos lados
#print("Os valores dos lados A e B do retângulo 1 são {} e {}, respectivamente".format(retangulo_01.Get_lado_A(),retangulo_01.Get_lado_B()))
#print("Os valores dos lados A e B do retângulo 2 são {} e {}, respectivamente \n".format(retangulo_02.Get_lado_A(),retangulo_02.Get_lado_B()))


# Alterando os valores dos lados
#retangulo_01.Set_lado_A(20)
#retangulo_01.Set_lado_B(2)
#retangulo_02.Set_lado_B(retangulo_01.Get_lado_A())

#print("Os novos valores dos lados A e B do retângulo 1 são {} e {}, respectivamente".format(retangulo_01.Get_lado_A(),retangulo_01.Get_lado_B()))
#print("Os novos valores dos lados A e B do retângulo 2 são {} e {}, respectivamente \n".format(retangulo_02.Get_lado_A(),retangulo_02.Get_lado_B()))


# Retorna calculo da área
#print("O valor da Área do reatangulo 1 é: {}".format(retangulo_01.Calcula_area()))
#print("O valor da Área do reatangulo 2 é: {}".format(retangulo_02.Calcula_area()))







