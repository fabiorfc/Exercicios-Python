# -*- coding: utf-8 -*-
"""
    1. Faça um programa que leia um arquivo texto contendo uma lista de 
endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP 
válidos e inválidos.

    O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

    O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
"""


# FUNÇÕES NECESSÁRIAS
#------------------------------------------------
# Função para salvar os ips válidos
def ips_validos(lista_ips):
    
    # Declaração do array
    ip_valido = []
    
    # Salvando os ips válidos
    for i in range(0, len(lista_ips)):
        if lista_ips[i] in lista_ips_validos:
            ip_valido.append(lista_ips[i])
    
    # Retornando o resultado
    return(ip_valido)

#------------------------------------------------
# Função para salvar os ips inválidos
def ips_nao_validos(lista_ips):
    
    # Declaração do array
    ip_nao_valido = []
    
    # Salvando os ips válidos
    for i in range(0, len(lista_ips)):
        if lista_ips[i] in lista_ips_nao_validos:
            ip_nao_valido.append(lista_ips[i])
    
    # Retornando o resultado
    return(ip_nao_valido)

#------------------------------------------------
# Gerando o arquivo de ips válidos
def arquivo_ips_validos(lista_ips):
    #Função que escreve o arquivo de ips válidos  
    with open('ips_validos.txt', 'w') as arquivo:
        for item in lista_ips:
            arquivo.write("%s\n" % item)     
    arquivo.close()
    
# Gerando o arquivo de ips nao válidos
def arquivo_ips_invalidos(lista_ips):
    #Função que escreve o arquivo de ips válido
    with open('ips_invalidos.txt', 'w') as arquivo:
        for item in lista_ips:
            arquivo.write("%s\n" % item)     
    arquivo.close()
    
    
 
    
    
# FUNÇÃO PRINCIPAL
# Endereço do link onde está o arquivo e nome do arquivo
link = 'C:\\Users\\fabicorrea\\Documents\\Estudos\\Python\\Lista de exercícios\\7) Exercícios com arquivos'
nome_arquivo = 'arquivo.txt'


#------------------------------------------------
# Listando os ips válidos e não válidos
lista_ips_validos = [['200.135.80.9'],['192.168.1.1'],['8.35.67.74'],['1.2.3.4']]
lista_ips_nao_validos = [['257.32.4.5'],['85.345.1.2'],['9.8.234.5'],['192.168.0.256']]


#------------------------------------------------
# Função para a leitura de arquivo
def leitura_arquivo(link, nome_arquivo):
    # Leitura do arquivo
    
    #Importando as libraries necessarias
    import os
    
    #Mudando o diretório
    os.chdir(link)
    
    # Declaração do array
    lista_ip = []
  
    
    # Leitura do arquivo
    file = open(nome_arquivo,'r') 
    for line in file:
        linha = line.split()
        lista_ip.append(linha)
    file.close()
    
    # Separando os ips
    lista_ips_validos = ips_validos(lista_ip)
    lista_ips_nao_validos = ips_nao_validos(lista_ip)

    #Gerando os arquivos com os ips
    arquivo_ips_validos(lista_ips_validos)
    arquivo_ips_invalidos(lista_ips_nao_validos)


#Testando a função
leitura_arquivo(link, nome_arquivo)


