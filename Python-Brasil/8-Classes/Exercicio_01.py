#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classe Bola: Crie uma classe que modele uma bola:
    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor
"""
class Bola:
    
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def Get_cor(self):
        return self.cor
    
    def Get_circunferencia(self):
        return self.circunferencia
    
    def Get_material(self):
        return self.material

    def Set_cor(self, cor):
        self.cor = cor

# Exemplos de bola
bola_01 = Bola(cor='azul', circunferencia=25,material='couro')
bola_02 = Bola(cor='amarelo', circunferencia=5,material='couro')
bola_03 = Bola(cor='verde', circunferencia=50,material='couro')

# Mostrando cores
print('Bola 1, tem cor: {}'.format(bola_01.Get_cor()))
print('Bola 2, tem cor: {}'.format(bola_02.Get_cor()))
print('Bola 3, tem cor: {}'.format(bola_03.Get_cor()))

# Trocando cores
bola_01.Set_cor('rosa')
bola_02.Set_cor('Vermelho')
bola_03.Set_cor(bola_01.Get_cor())

print('Depois da mudança, a Bola 1, tem cor: {}'.format(bola_01.Get_cor()))
print('Depois da mudança, a Bola 2, tem cor: {}'.format(bola_02.Get_cor()))
print('Depois da mudança, a Bola 3, tem cor: {}'.format(bola_03.Get_cor()))



