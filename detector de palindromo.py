frase = str(input('Digite a frase que você deseja para saber se é um Palíndromo: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = '' 
for c in range (len(junto)-1,-1,-1)