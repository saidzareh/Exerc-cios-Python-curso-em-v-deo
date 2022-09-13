num = int(input("coloque um número:"))
u = num//1%10
d = num//10%10
c = num//100%10
m = num//1000%10
print ('a unidade deste número é {}'.format(u))
print ('a dezena deste número é {}'.format(d))
print ('a centena deste número é {}'.format(c))
print (' o milhar deste número é {}'.format(m))
