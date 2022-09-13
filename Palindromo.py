frase = str(input('Digite uma frase para descobrir se ela é um palindromo:').strip().upper())
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1,-1):
    inverso += junto[letra]
print (junto, inverso)
if inverso == junto:
    print ('A frase é um palindromo!')
else:
    print ('a frase digitnada não é um palindromo')

