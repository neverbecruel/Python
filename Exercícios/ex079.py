lista_num = []
quero_continuar = 's'
while quero_continuar == 's':
    n = (int(input('Digite um valor: ')))
    if n not in lista_num:
        lista_num.append(n)
        print('Valor adicionado com sucesso! ')
    else:
        print('Valor duplicado! Não vou adicionar...  ')
    quero_continuar = input('Quer continuar? [S/N]').lower().strip()[0]
    if quero_continuar in 'nN':
        break
while quero_continuar not in 'SsnN':
    quero_continuar = input('Quer continuar? [S/N]').lower().strip()[0]
print('=-' * 30)
lista_num.sort()
print(f'Você digitou os valores {lista_num}')
