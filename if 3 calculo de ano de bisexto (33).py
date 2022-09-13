anobi = int(input('digite um ano para saber se ele é bisexto:'))
if anobi%100!=0 and anobi%4==0 or anobi%400==0:
    print ('o ano {} é bisexto'.format(anobi))
else:
    print ('o ano {} não é bisexto'.format(anobi))