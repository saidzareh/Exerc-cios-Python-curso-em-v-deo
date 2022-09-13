from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print (' PEDRA PAPEL OU TESOURA \n você contra o computador!')
print ('''Suas opções são:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Escolha sua jogada: '))
if jogador != (0,1,2):
    print ('jogue um número válido!')
print ('JO')
sleep (1)
print ('KEN')
sleep (1)
print ('PO!!')
sleep (1)
print ('-=*'*14)
print ('O jogador jogou {}'.format(itens[jogador]))
print ('O computador escolheu {}'.format((itens[computador])))
print ('-=*'*14)

if computador == 0:
    if jogador == 0:
        print('Empate! jogue novamente')
    elif jogador == 1:
        print ('Você ganhou!!!')
    elif jogador == 2:
        print ('O computador ganhou!!!')
    else:
        print ('jogue um número válido')
elif computador == 1:
    if jogador == 0:
        print ('Você perdeu!!') 
    elif jogador == 1:
        print ('Empate!! jogue novamente')
    elif jogador == 2:
        print ('Você ganhou!!!')
    else:
        print ('Jogue um número válido')
elif computador == 2:
    if jogador == 0:
        print ('Você ganhou!!')
    elif jogador == 1:
        print ('Você perdeu!!!')
    elif jogador == 2:
        print ('empate!!! jogue novamente.')
    else:
        print ('jogue um número válido')


   