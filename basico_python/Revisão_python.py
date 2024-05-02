# -*- coding: utf-8 -*-
"""
# Created on Sat Mar 23 19:10:07 2024

# @author: mathe
# """

# lista_vazia=[]
# lista=list()
# familia=["Daniel","matheus","ricardo"]

# familia.append('natalia')
# t1=tuple(["Rocha","Pedra", "Pedregulho"])

#Dicionarios

diconario={}

dicionari1o=dict()
familia={'Pai':'Roberto','Mae':'Bianca','Temfilhos':False}

familia2=dict(Pai="Carlos",Mae="Maria",Temfilhos=True)

listas_tuplas=[('Pai',"João"),("Mae","Julia"),("TemFilhos", False)]
familai3=dict(listas_tuplas)

# print(familia2["Pai"])
# print(familia2.values())


familia2["cachorro"]= "Todd"
familia2.update({"casa":False,"carro":True})
familia2.pop("carro")
familia2["cachorro"]= "Todd"
familia2['cachorro']='Tedy'
"Mae" in familia2
familia2["Animais"]= {'Cachorro','Gato','passaro'}

