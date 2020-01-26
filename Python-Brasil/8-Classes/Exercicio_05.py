#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: 
    número da conta, 
    nome do correntista e 
    saldo. 

Os métodos são os seguintes: 
    alterarNome, 
    depósito e 
    saque; 
    
No construtor, saldo é opcional, com valor default zero e os demais atributos 
são obrigatórios.
"""
class ContaCorrente:
    
    def __init__(self, cc_numero, correntista_nome):
        self.saldo = 0
        self.cc_numero = cc_numero
        self.correntista_nome = correntista_nome

    def __str__(self):
        return ">>> Conta {}. Correntista: {}. Saldo: {} <<<".format(self.cc_numero, self.correntista_nome, self.saldo)

    def altera_nome_correntista(self, nome):
        self.correntista_nome = nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

# Instancia classe teste
cliente = ContaCorrente(cc_numero = 2301, correntista_nome = 'Fabio')

# Verificacao da classe
print(cliente)

# Teste dos métodos
cliente.altera_nome_correntista("Joao da Silva")
cliente.deposito(50)
cliente.saque(40)
print(cliente)




