'''
Autor: Felipe Rottner Rodrigues
Data: 07/06/2024
Versão: 1.0
Descrição: Faça um programa que solicite para o usuário a senha de acesso
           ao sistema, ele terá no máximo três tentativas para inserir a
           correta cadastrada (senai115), caso passe desse limite uma mensagem 
           de erro deve aparecer.
           
'''
#================================================================================
senha = '' #var para receber a senha do ususario
senhaPadrao = 'senai115' #senha padrão do sistema
tentativa = 3 #número de tentativas de acesso 

while True:
    senha = input('Digite a sua senha: ') #senai115 => números com letras então sem casting

    if senha == senhaPadrao:
        print('Acesso liberado!')
        break #quebra o loop whilw, ou seja finalizar o programa
    else:
        tentativa = tentativa - 1 #tentaivas -= 1
        print('Você só possui mais', tentativa, 'tentativas')
    if(tentativa <= 0 ):
        print('Não possui mais tentativas')
        break