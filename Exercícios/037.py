num = int(input('digite um numero inteiro: '))
print('digite o numero referente ao tipo de converção')
print('binario [1]')
print('octal [2]')
print('hexadecimal [3]')
op = int(input('sua opção: '))
if op == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida')
