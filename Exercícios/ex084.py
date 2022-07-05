pessoas = list()
pessoa = list()
maior = menor = 0
c = 0
while True:
    pessoa.append(str(input('Digite o nome da pessoa: ')))
    pessoa.append(int(input('Digite o peso da pessoa: ')))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    c += 1
    resp = ' '
    while resp not in 'nNsS':
        resp = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if resp == 'n':
        break
print(f'Ao todo você cadastrou {c} pessoas')
print(f'O maior peso foi {maior}, de: ', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nA pessoa de maior peso é: ', end=' ')
print()
print(f'O menor peso foi {menor}, de: ', end='')
for n in pessoas:
    if n[1] == menor:
        print(f'[{n[0]}] ', end=' ')
