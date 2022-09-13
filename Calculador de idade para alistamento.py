from datetime import date
print('Coloque em que ano nasceu para saber se já está na hora de fazer seu alitamento militar')
ano = int(input('qual seu ano de nascimento?'))
data = (date.today().year)
idade = (data - ano)
if data-ano<18:
    print ('Você completa ou completou {} anos de idade e seu alistamento é daqui a {} anos'.format(idade,(18-idade)))
elif data-ano>18:
    print ('você completa ou completou {} anos de idade este ano e seu alistamento deveria ter sido feito a {} anos'.format(idade,(idade-18)))
else: print ('você deve fazer seu alistamento imeiatamente!')
