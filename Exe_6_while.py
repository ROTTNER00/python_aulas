'''
Autor: Felipe Rottner Rodrigues
Data: 07/06/2024
Versão: 1.0
Descrição: Estudos da estrutura de repetição "While"
#================================================
'''
indice = 1 
while indice < 17:
    print('Felipe', indice)
    indice = indice + 1 #indice += 1
#================================================
indice2 = 16
while indice2 > 0:
    print(indice2, 'Felipe')
    indice2 = indice2 - 1
#================================================
indice3 = 1
while True:
    print(indice3)
    indice3 = indice3 + 1
    if indice3 == 5:
        break
#================================================


while True:
    opcao = input('Digite S para finalizar o programa')
    #indice4 = indice4 + 1
    if opcao == 'S':
        break
