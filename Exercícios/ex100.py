from random import randint


def sorteador(lista):
    for c in range(5):
        c = randint(1, 6)
        lista.append(c)
    print(lista)


def somador(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos pares é {soma}.')


# num = [1, 2, 4, 45, 46, 7, 6, 3, 3, 32, 7, 8, 7, 67, 7777777777777]
numeros = []
sorteador(numeros)
somador(numeros)
