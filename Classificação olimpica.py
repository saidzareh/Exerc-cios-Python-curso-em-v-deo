from datetime import date
nasc = int(input('Coloque o ano de nascimento do atleta para saber que categoria ele pertence: '))
data = date.today().year
idade = (data-nasc) 
if idade<=9:
    print ("A categoria do seu filho é \033[1;32mMIRIM")
elif idade<=9: 
    print ('A sua idade é {} categoria do seu filho é \033[1;31minfantil.'.format(idade))
elif idade<=14: 
    print ('A sua {} e sua classificação é \033[1;33mjúnior'.format(idade))
elif idade<=19:
    print ('A sua idade é {} e sua classificação é \033[1;34msênior.'.format(idade))
else:
    print ('A sia odade é {} e sua classificação é \033[1;35mmaster'.format(idade))