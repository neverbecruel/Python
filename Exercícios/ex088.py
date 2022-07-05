import random
from time import sleep
jogos = []
pilha = []
print('-' * 30)
print('       JOGA NA MEGA SENA')
print('-' * 30)
quant = int(input('Quantos jogos quer que eu sorteie? '))
print(f' =-=-=-=SORTENDO {quant} JOGOS=-=-=-=')
for c in range(0, quant):
    while len(pilha) < 6:
        n = random.randrange(0, 60)
        if n not in pilha:
            pilha.append(n)
    jogos.append(pilha[:])
    pilha.clear()
for x in range(0, quant):
    print(jogos[x])
    sleep(1)
print('=-=-=- < BOA SORTE! > -=-=-=')
