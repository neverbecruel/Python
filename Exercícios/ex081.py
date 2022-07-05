lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resp = str(input('quer continuar? [S/N] ')).lower().strip()[0]
    if resp in 'nN':
        break
lista2 = lista[::]
lista2.sort(reverse=True)
print('-=' * 30)
print(f'Foram digitados {len(lista)} números.')
print(f'A lista em ordem decrescente ficou \n{lista2}')
if 5 in lista:
    print(f'O número 5 está na lista! ')
else:
    print('O número 5 não está na lista. ')
