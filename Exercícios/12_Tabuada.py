'''
Autor: Felipe Rottner Rodrigues
Data: 13/06/2024
Versão: 1.0
Descrição: Faça um programa que calcule a tabuada de um número digitado
           pelo usuário;
'''
#=====================================================================================
#variaveis
num_digitado = 0
numi = 0 
resultado = 0
num = 0
#Entrada
num_digitado = float(input('Insira o número de sua preferencia:'))

#Processamento 
for numi in range(10):#i < 11 (o até 10)
    #resultado = num_digitado * i
    num = num + 1
    print(f'{num_digitado} x {num} = {num_digitado * numi}') #interpolação