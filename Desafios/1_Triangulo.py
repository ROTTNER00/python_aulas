'''
Abertura do Comentário

Autor: Felipe Rottner Rodrigues
Data: 06/06/2024
Versão: 1.0
Descrição:   Faça um programa que recebe 3 valores e verifique se eles podem representar os lados em um triângulo
             1- Triângulo escaleno: triângulo que possui todos os lados com medidas diferentes.
             2- Triângulo isósoles: triângulo que possui dois lados com medidas iguais.
             3- Triângulo equilátero: triângulo que possui todos os lados com medidas iguais.

             Lembrando que a soma das medidas de dois lados de um triângulo é sempre maior que a medida do terceiro lado.


Fechamento do Comentário
'''
#================================================
#Variaveis
lado1 = 0
lado2 = 0
lado3 = 0
#Entrada
lado1 = float(input("Insira a medida do lado 1:"))
lado2 = float(input("Insira a medida do lado 2:"))
lado3 = float(input("Insira a medida do lado 3:"))
#Processamento
if lado1 + lado2 >= lado3 or lado1 + lado3 >= lado2 or lado3 + lado2 >= lado1:
    print("Esse triâmgulo não existe!")
elif lado1 == 0 and lado2 == 0 and lado3 == 0:
    print("Triângulo enexistente!")
elif lado1 == lado2 ==lado3: 
    print("Triângulo equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo isósoles")
elif lado1 != lado2 or lado1 != lado3 or lado2 == lado3:
    print("Triângulo escaleno")
#Saída 
