soma = quant = 0
while True:
    n = int(input('Digite um número: [999 para parar] '))
    if n == 999:
        break
    soma += n
    quant += 1
print('A soma dos {} valores foi {}!'.format(quant, soma))