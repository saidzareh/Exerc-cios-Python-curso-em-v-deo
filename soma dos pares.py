
soma = 0
count = 0
for c in range (1,7):
    n = int(input('digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        count += 1
print ('você informou {} números pares e a soma deles é {}'.format(count,soma))