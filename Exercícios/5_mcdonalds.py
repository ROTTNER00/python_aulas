'''
Abertura do Comentário

Autor: Felipe Rottner Rodrigues
Data: 04/06/2024
Versão: 1.0
Descrição: Descrição : Escreva um algoritino para exibir o nome do lanche
                       de acordo do número inserido pelo usuário, seguindo
                       a tabela abaixo:

                                      Nr. LANCHES
                                      1.  Big Mac
                                      2.  Quarteirão
                                      3.  McChicken
                                      4.  Cheddar McMelt
                                      5.  McFish


Fechamento do Comentário
'''
#================================================
#variavel
lanche = 0
#Entrada 
print('Escolha um dos lanches! \n 1.Big Mac \n 2.Quarteirão \n 3.McChicken \n 4.Cheddar McMelt \n 5.McFish')
lanche = int(input('Digite o número da sua ecolha:'))
#Processamento
if (lanche == 1):
    lanche_escolhido = 'Big Mac!'
elif (lanche == 2):
    lanche_escolhido = 'Quarteirão!'
elif (lanche == 3):
    lanche_escolhido = 'McChicken!'
elif (lanche == 4):
    lanche_escolhido = 'Cheddar McMelt!'
elif lanche == 5:
    lanche_escolhido = 'McFish!'
else:
    lanche_escolhido = 'Opção inválida!'
#Saída
print('O lanche escolhido foi:', lanche_escolhido)
#================================================