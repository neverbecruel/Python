from random import randint
from time import sleep

print('tente advinhar o numero entre 0 e 10 em que estou pensando...')
tent = int(input('Qual é a sua tentativa? '))
sleep(0.2)
o = randint(0, 10)
palpites = 0
while tent != o:
    palpites += 1
    print('PROCESSANDO...')
    sleep(0.2)
    tent = int(input('errou, tente denovo: '))
print('Parabéns, você acertou com {} tentativas!!!'.format(palpites))
# 29:10
