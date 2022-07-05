n = int(input('Digite um número: [999 para parar] '))
cont = 0
soma = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número: [999 para parar] '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))