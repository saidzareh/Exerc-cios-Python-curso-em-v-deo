from math import radians,sin,cos,tan
ang = float(input('digite o angulo que você deseja:'))
print ('o angulo de {} tem o seno {:.2f} \n o angulo de {} tem o cosseno {:.2f} \n o angulo de {} tem a tangente {:.2f}'.format(ang,sin(radians(ang)),ang,cos(radians(ang)),ang,tan(radians(ang))))