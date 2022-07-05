#leia um programa q leia um número e leia o seu fatorial.
from time import sleep
'''n = int(input('Digite o número que você deseja saber o fatorial: '))
r = 1
ac= n
for c in range(n, 0, -1):
    ac -= 1
    print(c, 'x', ac, end='')'''
n = int(input('Digite o número que você deseja saber o fatorial: '))
cont = n
fatorial = 1
print(f'CALCULANDO {n}!... ')
sleep(0.7)
while cont > 0:
    print(f'{cont} ', end='')
    print('x ' if cont > 1 else '= ', end='')
    fatorial = fatorial * cont
    cont -= 1
print(f'{fatorial}')
