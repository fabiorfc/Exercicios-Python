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
from Exercicio_03_retangulo import retangulo


print("Informe as dimensões do local que deseja colocar pisos")
largura_01 = input("Informe o valor da primeira dimensão: \n")
largura_02 = input("Informe o valor da segunda dimensão: \n")


usuario_01 = retangulo(lado_A = largura_01, lado_B = largura_02)

print("\n")
print("Você irá precisar de um total de pisos para preencher:")
print("Uma área de {}".format(usuario_01.Calcula_area()))
print("Um rodapé de {}".format(usuario_01.Calcula_perimetro()))

