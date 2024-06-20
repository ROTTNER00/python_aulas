'''
Autor: Felipe Rottner Rodrigues
Data: 17/06/2024
Versão: 1.0
Descrição: Faça um programa que adicione alunos ao sistema da escola
           (array) ou remova um aluno especifico.
           Nesse sistema deve estar previsto um com três opções:
           #============================================================
           Sistema SENAI
           1 - Adicionar aluno:
           2 - Remover aluno:
           3 - Sair
           Insir a opção desejada:
           #============================================================
           Adicionar aluno
           Insira o nome do aluno:
           #============================================================
           Remover aluno
           Insira o nome do aluno para ser removido:
           #============================================================
           Alunos no sistema
           ['João', 'Pedro', 'Luana']
           
'''
#=====================================================================================
opcao = 0
alunos_sistema = []
print(alunos_sistema)

while True:
    print('Sistema SENAI \n 1 - Adicionar aluno: \n 2 - Remover aluno: \n 3 - Sair')
    opcao = int(input('Escolha uma opção:'))
    if opcao == 1:
        alunos_sistema.append(input('Digite um nome do aluno que queira adicionar:'))
        print(alunos_sistema)
    elif opcao == 2:
        alunos_sistema.remove(input('Digite o nome que você queira remover:'))
        print(alunos_sistema)
    elif opcao == 3:
        print(alunos_sistema)
    else:
        break
        