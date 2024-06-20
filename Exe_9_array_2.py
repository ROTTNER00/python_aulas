'''
Autor: Felipe Rottner Rodrigues
Data: 17/06/2024
Versão: 1.0
Descrição: Estudos do tipo de dado Array
'''
#=====================================================================================
carros = ['VW']

carros.append('GM')#adiciona na última posição o valor indicado
carros.append('Ford')
carros.append('Fiat')
carros.append('Renault')
print(carros)

carros.remove('Ford')#Remove item indicado o valor
print(carros)

carros.pop(3)#Remove item indicando index
print(carros)

print(len(carros))#Tamanho do vetor atual

carros.pop(len(carros) -1)#Deleta sempre a última posição do array
print(carros)