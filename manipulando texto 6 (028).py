nome = str(input('coloque seu nome:').strip())
n = nome.split()
print ('seu primeiro nome é {}'.format(n[0]))
print ('seu segundo nome é {}'.format(n[len(n)-1]))