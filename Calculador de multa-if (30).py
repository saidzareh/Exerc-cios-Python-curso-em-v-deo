velocidade = (int(input("digite a velocidade atual do carro:")))
if velocidade >80:
    print('MULTADO! a velocidade máxima é 80km, o valor da sua multa é {} reais'.format((velocidade - 80) * 7))

if velocidade<=80:
    print ('dirija com segurança!')