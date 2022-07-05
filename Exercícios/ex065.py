cond = 's'
soma = quant = media = maior = menor = 0
while cond in 'sS':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cond = str(input('Quer continuar? [S/N] ')).upper().lower()[0]
media = soma / quant
print('Você digitou {} números e a média entre eles foi de {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

'''n1 = n = int(input('Digite um número: '))
cond = input('Quer continuar? [S/N] ').strip().lower()
if cond == 'n':
    print('Você digitou 1 números e a média foi {}'.format(n))
soma = 0
while cond == 's':
    soma += n
    n = int(input('Digite um número : '))
    cond = input('Quer continuar? [S/N] ').strip().lower()
    if cond == 'n':
        print(soma + n1)'''
