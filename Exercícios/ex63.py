print('~~' * 18)
print('     SEQUÊNCIA DE FIBONACCI')
print('~~' * 18)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print('-> {}'.format(t3), end='')
print(' -> FIM ')
print('--' * 18)
