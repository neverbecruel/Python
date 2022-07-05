numeros = list()
pares = list()
impares = list()
teste = list()
cont1 = 1
for c in range(0, 7):
    teste.append(int(input(f'Digite o {cont1}º valor: ')))
    cont1 += 1
for par in teste:
    if par % 2 == 0:
        pares.append(par)
pares.sort()
for impar in teste:
    if impar % 2 != 0:
        impares.append(impar)
impares.sort()
numeros.append(pares[:])
numeros.append(impares[:])
impares.clear()
pares.clear()
print(f'Os números pares que você digitou foram: {numeros[0]}')
print(f'OS numeros impares que você digitou foram: {numeros[1]}')
