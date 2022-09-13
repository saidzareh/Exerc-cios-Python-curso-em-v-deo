import random 
print ('Pedra papel e tesoura')
print (''' [0] Pedra
           [1] Papel
           [2] Tesoura''')
pessoa = (int(input('Escolha o numero referente a sua opção')))
pc = random.randint(0,1,2)
print (pessoa,pc)
