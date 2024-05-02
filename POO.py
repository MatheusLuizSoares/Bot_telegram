# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:04:07 2024

@author: mathe
"""

#POO

class Veiculo:
    def __init__(self,nome,tipo):
        self._nome=nome
        self._tipo=tipo

    def tipoVeiculo(self):
        print(self._nome)
    

v2=Veiculo("caminhão","Terrestre")
v2.tipoVeiculo()
moto=Veiculo("Honda","Terrrestre")
barco=Veiculo("Barco pequeno","Maritimo")
             
