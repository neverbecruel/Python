lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'{n} dicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'{n} adicionado na posição {pos}')
                break
            pos += 1
print('Os valores digitados em ordem crescente ficou:')
print(lista)
