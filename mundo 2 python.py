vcasa = int(input('Vamos calcular as prestações da sua casa nova? qual o valor da casa que você quer comprar?'))
vsalario = (int(input('quanto você recebe por mês?')))
vanos = (int(input('Em quantos anos gostaria de pagar essa casa?')))
prestcasa = (vcasa/(vanos*12))
prestmax = (vsalario*0.3)

if prestcasa < prestmax:
    print ('O valor das prestações é {:.2f} e com seu salário você foi aprovado na compra desta casa nesta quantidade de parcelas, parabéns!'.format(prestcasa))
elif prestcasa >= prestmax:
        print ('Infelizmente com seu salário atual sua compra não pode ser aprovada, tente parcelar mais vezes.')