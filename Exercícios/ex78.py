valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posção {c}: ')))
print(f'Você digitou os valores {valores}')
valore = valores[:]
valore.sort()
print(f'O maior valor digitado foi {valore[4]}, e se encontra nas posições: ', end='')
for indice, valor in enumerate(valores):
    if valor == valore[4]:
        print(f'{indice} ', end='')
print(f'\nO menor valor digitado foi {valore[0]}, e se encontra nas posições: ', end='')
for indicem, valorm in enumerate(valores):
    if valorm == valore[0]:
        print(f'{indicem}...', end='')


