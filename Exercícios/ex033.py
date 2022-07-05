a = int(input('digite um numero: '))
b = int(input('digite um numero: '))
c = int(input('digite um numero: '))
# menorrr
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    c = menor
# maiorr
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o maior número é {} e o menor é {}'.format(maior, menor))
