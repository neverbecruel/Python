from random import randint as rd
print('=-' * 17)
print('VAMOS JOGAR PAR OU IMPAR? ')
print('=-' * 17)
cont = 0
while True:
    n = int(input('Digite um número: '))
    pi = ' '
    print('=-' * 17)
    pc = rd(0, 10)
    soma = n + pc
    while pi not in 'pPiI':
        pi = str(input('Par ou ímpar? [P/I] '))
    if pi in 'pP':
        if soma % 2 != 0:
            print(f'Você jogou {n} e o computador {pc}, deu ímpar \nVocê perdeu:( ')
            print('=-' * 17)
            break
        else:
            print(f'Você jogou {n} e o computador {pc}, deu par  \nParabens!')
            print('Vamos jogar novamente. ')
            print('=-' * 17)
            cont += 1
    if pi in 'Ii':
        if soma % 2 != 0:
            print(f'Você jogou {n} e o computador {pc}, deu ímpar \nParabens!')
            cont += 1
            print('Vamos jogar novamente. ')
            print('=-' * 17)
        else:
            print(f'Você jogou {n} e o computador {pc}, deu par \nVocê perdeu :( ')
            print('=-' * 17)
            break
print(f'GAME OVER. Você venceu {cont} vezes.')


