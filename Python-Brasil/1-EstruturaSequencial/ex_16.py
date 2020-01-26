#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
16. Faça um programa para uma loja de tintas. O programa deverá pedir o 
tamanho em metros quadrados da área a ser pintada. Considere que a cobertura 
da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em 
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de 
latas de tinta a serem compradas e o preço total.
"""

from math import ceil

print(">>> Informe a Área a ser pintada <<<")
area = input("Em metros quadrados: ")

litros_de_tinta = float(area) / 3
latas_de_tinta = ceil(litros_de_tinta/18)
preco_a_ser_pago = latas_de_tinta * 80

print(">>> Para a área em questão serão usados: <<<")
print("{} Latas de tinta".format(latas_de_tinta))
print("O custo final será de: R$ {}".format(preco_a_ser_pago))