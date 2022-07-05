total = tot1000 = menor = cont = 0
mepre = ' '
print('--' * 16)
print('      LOJA SUPER BARATÃO')
print('--' * 16)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        tot1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        mepre = produto

    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if resp == 'n':
        break
print(f'O preço total foi de R${total:.2f}')
print(f'{tot1000} produtos custaram mais de R$1000.00')
print(f'O produto mais barato foi a {mepre}, custou {menor:.2f}')
