nome = str(input('coloque uma frase:').strip())
print ('a sua frase tem a letra A {} vezes:'.format(nome.lower().count("a")))
print ('A primeira letra A apareceu na posição {}'.format(nome.lower().find('a') + 1))
print ('A última letra A aparece na posição {}'.format(nome.lower().rfind('a') +1))