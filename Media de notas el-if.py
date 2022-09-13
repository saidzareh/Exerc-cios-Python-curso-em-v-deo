nota1 = float(input('Coloque a primeira nota do aluno:'))
nota2 = float(input('coloque a segunda nota do aluno:'))
nota3 = float(input('coloque a terceira nota do aluno::'))
media = (nota1+nota2+nota3)/3 
if media<=5:
    print ('o aluno foi reprovado sua media foi {:.1f}'.format(media))
elif media>=5 and media<7:
    print ('o aluno está em recuperação, sua meia foi {:.1f}'.format(media))
elif media>=7:
    print ('o aluno passou de ano, sua média foi {:.1f}'.format(media))
