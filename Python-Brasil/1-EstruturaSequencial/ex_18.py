#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    18 - Faça um programa que peça o tamanho de um arquivo para download 
(em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o 
tempo aproximado de download do arquivo usando este link (em minutos).
"""

print(">>> Informe o tamanho do arquivo e a velocidade da internet <<<")
tamanho_do_arquivo = input("Tamanho do arquivo (Em MB): ")
velocidade_da_internet = input("Velocidade da internet (Em Mbps): ")

tamanho_do_arquivo = float(tamanho_do_arquivo)
velocidade_da_internet = float(velocidade_da_internet)

tempo_de_transferencia = tamanho_do_arquivo / velocidade_da_internet
tempo_de_transferencia_em_minutos = tempo_de_transferencia / 60

print("\n O arquivo será baixado em {0:.4f} minutos".format(tempo_de_transferencia_em_minutos))


