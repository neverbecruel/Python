t = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {t}')
print(f'O número 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O valor 3 foi digitado na posição {t.index(3)+1}')
else:
    print(f'O valor 3 não foi digitado. ')
print('Os valores pares digitados: ', end='')
for c in t:
    if c % 2 == 0:
        print(c, end=' ')
