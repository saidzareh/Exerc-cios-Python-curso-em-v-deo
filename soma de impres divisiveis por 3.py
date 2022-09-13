count = 0
soma = 0
for c in range (1,501,2):
    if c % 3 == 0:
        soma = soma + c
        count = count + 1 
print ('A soma de todos  os valores solicitados é {}.'.format(soma))
print ('A quantidade de números é {}'.format(count))