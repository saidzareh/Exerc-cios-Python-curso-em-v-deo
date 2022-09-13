from datetime import date
anoatual = date.today().year 
totmaior = 0
totmenor = 0
for pess in range (1,8):
    nasc = int(input(f'Coloque o ano em que a {pess}ª pessoa nasceu:'))
    idade = anoatual-nasc 
    if idade>=21:
        totmaior +=1
    if idade<21:
        totmenor +=1
print (f'o número de pessoas de maior é {totmaior} \n e o número de pessoas menor é {totmenor}')

