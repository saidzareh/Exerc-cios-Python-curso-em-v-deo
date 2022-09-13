salario = float(input('digite o valor do seu salário para saber seu aumento:'))
if salario <= 1250:
    print('o seu salário agora será {:.2f}R$'.format(salario*1.15))
else:
    print('o eu salário agora será de {:.2f}R$'.format(salario*1.10))