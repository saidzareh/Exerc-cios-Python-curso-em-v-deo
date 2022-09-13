viagem = float(input('diga a distância da sua viagem em KM para saber o valor dela'))
if viagem <= 200:
    print ('o valor da sua viagem é {:.2f}R$'.format(viagem*0.5))
else:
    print ('o valor da viagem é {:.2f}R$'.format(viagem*0.45))