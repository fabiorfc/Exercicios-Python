#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    7 - Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi 
(Bichinho Eletrônico):

a. Atributos: 
    Nome, Fome, Saúde e Idade 

b. Métodos: 
    Alterar Nome, Fome, Saúde e Idade; 
    Retornar Nome, Fome, Saúde e Idade 
    
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do 
nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, 
ou seja, um campo calculado, então não devemos criar um atributo para armazenar
 esta informação por que ela pode ser calculada a qualquer momento.

"""
from random import randint

class Tamagushi:
    
    def __init__(self, nome):
        self.nome = nome
        self.fome = randint(0,10)
        self.saude = randint(0,100)
        self.idade = 0
        
    def __str__(self):
        if self.fome == 0:
            humor = 50 * ( 1 + self.saude/100)
        else:
            humor = 50 * ((1-self.fome/10) + self.saude/100)
        return " >>> {} \n Fome: {} \n Saude: {} \n Idade {} \n Humor: {}%".format(self.nome, self.fome, self.saude, self.idade, humor)

    def alterar_nome(self, nome):
        self.nome = nome
    
    def alimenta_tamagushi(self, alimento):
        print("\n {} depois da refeição".format(self.nome))
        if self.fome < alimento:
            self.fome = 0
        else:
            self.fome -= alimento

    def leva_tamagushi_no_medico(self):
        print("\n {} depois do médico".format(self.nome))
        self.saude += randint(0,100)
        if self.saude > 100.0:
            self.saude = 100.00
    
    def passa_ano(self):
        print("\n Feliz aniversário para o {}".format(self.nome))
        self.idade += 1
        


# Instanciando o Tamagushi
madruguinha = Tamagushi("Madruguinha")

# Verificando o objeto
print(madruguinha)
    
# Testando os métodos
madruguinha.alterar_nome("Madruguinha da Silva")
print(madruguinha)

# Alimentando o madruguinha
madruguinha.alimenta_tamagushi(4)
print(madruguinha)

# Levando madruguinha ao médico
madruguinha.leva_tamagushi_no_medico()
print(madruguinha)

# Levando madruguinha ao médico
madruguinha.passa_ano()
print(madruguinha)

