print ('{:=^40}'.format(' Lojas Compre Mais '))
preço = float(input('Coloque o valor das suas compras:'))
print ('''FORMAS DE PAGAMENTO
[\033[1;32m1\033[m] A vista com 10 porcento de desconto
[\033[1;32m2\033[m] A vista no cartão com 5 porcento de desconto
[\033[1;32m3\033[m] em até 2x no cartão sem juros
[\033[1;32m4\033[m] de 3x a 10x no cartão com 20 porcento de juros\n''')
opção = int(input('Digite o número da opção para escolher a forma de pagamento?'))
if opção == 1:
    print ('O valor final da sua compra é {}R$ com 10% de desconto'.format(preço*0.9))
elif opção == 2:
    print ('O valor final da sua compra é {}R$ com 5% de desconto'.format(preço*0.95))
elif opção == 3:
    print ('O valor foi dividido em 2 parcelas de {}R$'.format(preço/2))
elif opção ==4: 
    div = int(input('Em quantas vezes deseja dividir o valor?'))
    print('O valor final do produto dividido em {} parcelas é {} em {} parcelas de {}'.format(div,(preço*1.2),div,(preço*1.2)/div))
else:
    print('digite um numero válido entre 1 e 4.')