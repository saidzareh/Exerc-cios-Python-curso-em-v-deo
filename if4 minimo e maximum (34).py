a = int(input('coloque o primeiro número:'))
b = int(input('coloque o segundo número:'))
c = int(input('coloque o terceiro número'))
    #metodo mais simples
#maneira mais simples de fazer
#print('o menor número digitado foi', min(a,b,c))
#print('o maior número digitado foi', max(a,b,c))

 #usando if para o menor
menor = a
if b<c and b<a:
   menor=b
if c<a and c<b:
   menor = c

 #usando if para o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print ('o maior valor digitado é {}'.format(maior))
print ('o menor valor digitado é {}'.format(menor))