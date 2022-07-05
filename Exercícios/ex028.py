import random
from time import sleep
print('Tente advinhar o número entre 0 e 5.')
x=random.randint(0,5)
game = int(input('Tente. Digite um número: '))
print('PROCESSANDO...')
sleep(2)
if game == x:
    print('Parabéns, você acertou.')
else:
    print('Você errou.')

