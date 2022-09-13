from random import randint
from time import sleep

print ('O computador vai sortear um número de 0 a 5, tenta adivinhar o número')
hn = int(input('Qual número de o a 5 você quer escolher?'))
cn = randint(1,5)
print ('Processando')
sleep(3)
print ('O número do computador foi {}'.format(cn))
if cn==hn:
      print ('parabéns, você acertou!')
else: print ('infelizmente você não acertou... tente outra vez!')
