t1 = int(input('Digite o primeiro termo da P.A. '))
razao = int(input('Digite a razão da P.A. '))
cont = 1
print(t1, end=' -> ')
while cont < 10:
    pa = t1 = t1 + razao
    print(pa, end=' -> ')
    cont += 1
print('ACABOU ')
