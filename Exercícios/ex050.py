soma = 0
cont = 0
for c in range(1, 7):
    val = int(input(' digite o {} valor: '.format(c,)))
    if val % 2 == 0:
        soma += val
        cont += 1
print('vc informou {} números pares e a soma entre eles é {}'.format(cont, soma))
