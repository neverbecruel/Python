a = int(input('digite um numero: '))
b = int(input('digite outro numero: '))
if a > b:
    print('o numero {} é maior que o numero {}'.format(a, b))
elif b > a:
    print('o numero {} é maior q o numero {}'.format(b, a))
else:
    print('os numeros {} e {} são iguais'.format(a, b))