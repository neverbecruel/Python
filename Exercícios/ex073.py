from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10),
        randint(1, 10), randint(1, 10))
# jeito ruim de achar o maior e o menor

'''maior = tupla[0]
menor = maior
if tupla[1] > maior:
    maior = tupla[1]
if tupla[2] > maior:
    maior = tupla[2]
if tupla[3] > maior:
    maior = tupla[3]
if tupla[4] > maior:
    maior = tupla[4]
elif tupla[0] < menor:
    menor = tupla[0]
elif tupla[1] < menor:
    menor = tupla[1]
elif tupla[2] < menor:
    menor = tupla[2]
elif tupla[3] < menor:
    menor = tupla[3]
elif tupla[4] < menor:
    menor = tupla[4]
print(f'O maior valo sorteado foi {maior}, e o menor foi {menor}')
'''
# jeito mais pratico
print(tupla)
print(f'O maior valo sorteado foi {max(tupla)}, e o menor foi {min(tupla)}')
