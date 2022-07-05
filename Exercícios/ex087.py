# confundi tudo

valores = [[], [], []]
par = col3 = 0
for x in range(0, 3):
    for y in range(0, 3):
        valores[x].append(int(input(f'Digite o valor da posição {x, y}: ')))
        par += valores[x][y] if valores[x][y] % 2 == 0 else 0
        col3 += valores[x][y] if y == 2 else 0
print(*valores, sep='\n')
print(f'A soma dos valores pares foi: {par}')
print(f'A soma dos valores da 3ª coluna é: {col3}')
print(f'O maior valor da segunda linha é {max(valores[1])}')