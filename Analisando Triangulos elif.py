print ('Coloque os lados do triangulo para saber seu tipo.')
l1 = int(input('primeiro lado: '))
l2 = int(input('segundo lado: '))
l3 = int(input('terceiro lado: '))
if l1<l2+l3 and l2<l1+l3 and l3<l2+l1:
    print ('A junção desses lados pode formar um triangulo!')
    if l1==l2==l3:
        print (' Este triangulo é equilatero!')
    elif (l1==l2 or l1==l3 or l2==l3) and (l1!=l2 or l1!=l3):
        print ('este triangulo é isoscles')
    elif l1!=l2 and l2!=l3:
        print ('este triangulo é esclaeno')
else:
    print('Estes valores não podem formar um triangulo')

