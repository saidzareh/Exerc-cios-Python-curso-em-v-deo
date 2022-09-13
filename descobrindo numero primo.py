n = (int(input('Coloque um número para descobrir se ele é primo:')))
tot = 0
for c in range (1,n+1):
    if n%c==0:
        print ('\033[1;33m', end='')
        tot += 1
    else: 
        print ('\033[1;31m', end='')
    print ("{}".format(c),end=' ')
print (f'\033[m\n o número {n} é divisível {tot} vezes!')
if tot == 2:
    print ('por isto ele é um número primo!')
else:
    print ('por isto ele não é primo!')

