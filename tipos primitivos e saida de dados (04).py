print ('=-=-='*12)
n = input('\033[1;97mdigite algo:\033[m')
print ('=-=-='*12)
print('o que você digitou é uma letra e/ou numero?', n.isalnum())
print('o que você digitou é um numero?' ,n.isnumeric())
print('o que você digitou é uma letra?',n.isalpha())
print ('O que você digitou está em maiusculo e/ou minusculo', n.isascii())
print ('o que você difitou está em apenas maiusculo?', n.isupper()),
print ('o que você digitou está em apenas minusculo?', n.isprintable())