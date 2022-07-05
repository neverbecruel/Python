lista1 = []
listapares = []
listaimpar = []
while True:
    n = int(input('Digite um valor: '))
    lista1.append(n)
    resp = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if resp == 'n':
        break
print(f'A lista digitada é: {lista1}')
for c in range(len(lista1)):
    if lista1[c] % 2 == 0:
        listapares.append(lista1[c])
print(f'A lista de pares é: {listapares}')
for y in range(len(lista1)):
    if lista1[y] % 2 == 1:
        listaimpar.append(lista1[y])
print(f'A lista de impares ficou: {listaimpar}')




