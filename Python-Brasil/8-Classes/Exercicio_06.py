#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    6) Classe TV: Faça um programa que simule um televisor criando-o como um 
objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou 
diminuir o volume. Certifique-se de que o número do canal e o nível do volume 
permanecem dentro de faixas válidas.
"""
class TV:
    
    def __init__(self):
        self.volume = 6
        self.canal = 3
    
    def __str__(self):
        return " >>> Canal {}. Volume {} <<< ".format(self.canal, self.volume)

    def muda_canal(self, canal):
        if canal < 0:
            pass
        elif canal >= 100:
            pass
        else:
            self.canal = canal

    def muda_volume(self, volume):
        if volume < 0:
            self.volume = 0
        elif volume > 20:
            self.volume = 20
        else:
            self.volume = volume

        
# Instanciando a TV
televisor = TV()

# Verificando objeto
print(televisor)

# Mudando de canal
televisor.muda_canal(15)
televisor.muda_volume(20)
print(televisor)

televisor.muda_canal(156)
televisor.muda_volume(100000)
print(televisor)

