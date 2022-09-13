print ('Coloque o valor de três retas para descobrir se elas formariam um triangulo.')
r1 = float(input('reta 1:'))
r2 = float(input('reta 2:'))
r3 = float(input('reta 3:'))
R = max(r1,r2,r3)

if R > (r1+r2+r3)-R:
    print ('Estas três retas não podem formar um triangulo')
if R <= (r1+r2+r3)-R:
    print ('estas três retas podem formar um triangulo')
