import random

aluno1 = input('coloque o nome do primeiro aluno:')
aluno2 = input('coloque o nome do segundo aluno:')
aluno3 = input('coloque o nome do terceiro aluno:')
aluno4 = input('coloque o nome do quarto aluno:')
lista = [aluno1,aluno2,aluno3,aluno4]
print ('o aluno escolhido é {}'.format(random.choice(lista)))
