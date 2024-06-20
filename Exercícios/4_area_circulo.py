#===========================================================================================
#Autor: Felipe Rottner Rodrigues
#Data: 28/05/20024
#Versão: 1.0 
#Descrição: Faça umalgoritimo que receba a o raio em metros 
#           de um círculo e apresente a sua área
#           ----------------------------------------------------
#           Exemplo de execução
#           Insira o raio em metros: 5
#           Área do circulo: 78.5m^2
#           a = área
#           pi = 3.14
#           r = raio
#           a = pi*(r^2)
#===========================================================================================
#Início
#variaveis
r = 0 #raio
a = 0 #área
pi = 3.14 #constante pi
#Entrada
print('Calcular a área do circulo!')
r = float(input('Digite o valor do raio:'))
#processamento
a = pi*(r**2)
#Saída
print('A área do círculo é:', a, 'm^2')