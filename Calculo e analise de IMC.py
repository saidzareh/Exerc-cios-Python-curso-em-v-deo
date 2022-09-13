print ('Para saber ser IMC coloque seu peso e altura.')
peso = float(input('qual seu peso em Kg? '))
altura = float(input('qual sua altura em Metros?'))
imc = peso/(altura**2)

if imc < 18.5:
    print ('você está abaixo do peso, seu imc é {:.1f}'.format(imc))
elif imc > 18.5 and imc <= 25:
    print ('Você está no seu peso normal, seu IMC é {:.1f}'.format(imc))
elif imc > 25 and imc <= 30:
    print ('Você está com sobrepeso, seu imc é {:.1f}'.format(imc))
elif imc > 30 and imc <= 40:
    print ('Você está com obesidade, seu imc é {:.1f}'.format(imc))
else:
    print ('Você está com obesidade morbida, seu imc é {:.1f}'.format(imc))

