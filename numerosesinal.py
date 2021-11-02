n1 = int(input('INSIRA O PRIMEIRO NUMERAL: '))
sinal = input('DIGITE O SINAL: ')
n2 = int(input('INSIRA O SEGUNDO NUMERAL: '))

if sinal == '+':
    op = n1 + n2
elif sinal =='-':
    op = n1 - n2
elif sinal == '*':
    op = n1 * n2
elif sinal == '/':
    op = n1 / n2
else:
    print('SINAL INCORRETO')

print(op)


