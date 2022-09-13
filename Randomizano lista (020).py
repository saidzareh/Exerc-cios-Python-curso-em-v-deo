import random
aluno1 = input('coloque o nome do primeiro aluno:')
aluno2 = input('coloque o nome do segundo aluno')
aluno3 = input('coloque o nome do terceiro aluno')
aluno4 = input('coloque o nome do terceiro aluno')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('a ordem de apresentação é:',lista)

