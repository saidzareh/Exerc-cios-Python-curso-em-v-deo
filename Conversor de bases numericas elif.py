numero = int(input('digite um número inteiro:'))
print ('''escolha uma da bases para conversão'
[ 1 ] converter para \033[1;93mbinario\033[m
[ 2 ] converter para \033[1;93moctal\033[m
[ 3 ] converte para  \033[1;93mhexadecimal\033[m''')
opção = int(input(' digite a sua opção: '))
if opção == 1:
    print ('{} convertido para binario é igual a {}.'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print ('{} convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print ('{} convertido para hexadecimal é igual a {}'.format(numero,hex(numero)[2:]))
else:
        print('opção invalida, escolha 1, 2 ou 3.')
