from time import sleep


def maior(* num):
    cont = maior = 0
    print('=-' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f' {valor}', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
        sleep(0.3)
    print(f'. Foi informado {cont} valores')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
