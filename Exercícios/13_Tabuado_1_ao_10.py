'''
Autor: Felipe Rottner Rodrigues
Data: 13/06/2024
Versão: 1.0
Descrição: Faça um programa que apresente a tabuada 1 ao 10;
'''
#=====================================================================================
for i in range(11):#0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
    for j in range(11):#0 -> 10
        print(f'{i} x {j} = {i * j}')
    print('=====================================================================================')