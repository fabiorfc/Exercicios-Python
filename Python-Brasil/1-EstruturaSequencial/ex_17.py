#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o 
tamanho em metros quadrados da área a ser pintada. Considere que a cobertura 
da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em 
latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam 
R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos 
preços em 3 situações:
    - comprar apenas latas de 18 litros;
    - comprar apenas galões de 3,6 litros;
    - misturar latas e galões, de forma que o preço seja o menor. Acrescente 
10% de folga e sempre arredonde os valores para cima, isto é, considere latas 
cheias.
"""

from math import ceil

print(">>> Informe a Área a ser pintada <<<")
area = input("Em metros quadrados: ")

litros_de_tinta = round(float(area) / 6, 2)

# Calculo da Situacao 1
lata_situacao_01 = ceil(litros_de_tinta/18)
preco_situacao_01 = lata_situacao_01 * 80
# Calculo da Situacao 2
lata_situacao_02 = ceil(litros_de_tinta/3.6)
preco_situacao_02 = lata_situacao_02 * 25
# Calculo da Situacao 3
lata_de_18_litros = int(litros_de_tinta/18)
lata_de_3p6_litros = ceil((litros_de_tinta % 18) / 3.6)
preco_situacao_03 = lata_de_18_litros * 80 + lata_de_3p6_litros * 25

print("\n >>> Para a área em questão serão usados {} litros de tinta <<<".format(litros_de_tinta))
print("\n >>> As opções são: <<<")
print("Comprar {} lata(s) de 18 litros ao custo de R$ {}".format(lata_situacao_01, preco_situacao_01))
print("Comprar {} lata(s) de 3,6 litros ao custo de R$ {}".format(lata_situacao_02, preco_situacao_02))
print("Comprar {} e {} lata(s) de 18 e 3,6 litros, respectivamente, ao custo de R$ {}".format(lata_de_18_litros, lata_de_3p6_litros,preco_situacao_03))



