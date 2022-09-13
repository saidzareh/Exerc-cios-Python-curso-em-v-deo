from datetime import date
from smtpd import MailmanProxy
somai = 0
somam = 0
maior=0
menor=0
M = 1
for c in range (1,4):
    print ('-=-'*10, f'{c}ª PESSOA', '-=-'*10)
    nome = str(input('Qual sue nome: '.capitalize()))
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo?[M/F]: '.upper()))
    somai = somai+idade
    if sexo == M:
        somam=somam+1
    if c==1:
        maior = idade
        menor = idade
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade
print (somai/3,somam)

# VAI CANDAO


