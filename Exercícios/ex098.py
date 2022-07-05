from time import sleep

'''print('=-' * 20)
print('Contagem de 1 até 10 de 1 em 1')
for c in range(10):
    sleep(0.3)
    print(f' {c + 1}', end='')
sleep(0.3)
print(' FIM!')
print('=-' * 20)
print('Contagem de 10 até 0 de 2 em 2')
sleep(1)
for c in range(10, 0, -2):
    sleep(0.3)
    print(f' {c}', end='')
    sleep(0.3)
print(' FIM!')
print('=-' * 20)
print('Agora é sua vez de personalizar a contagem')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('=-' * 20)
print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
if inicio > fim and passo > 0:
    passo = passo - 2 * passo
for c in range(inicio, fim, passo):
    sleep(0.3)
    print(f' {c}', end='')
sleep(0.3)
print(' FIM!')
print('=-' * 20)'''


def contagem(inicio, fim, passo):
    pao = passo
    if passo == 0:
        pao = 1
    if passo < 0:
        passo = passo * -1
    if inicio > fim and passo > 0:
        pao = passo - passo * 2
    print('=-' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}...')
    for c in range(inicio, fim + 1, pao):
        sleep(0.3)
        print(f' {c}', end='')
    print(' FIM!')


contagem(1, 10, 1)
contagem(10, 0, -2)
print('Agora é sua vez de personalizar a contagem...')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
