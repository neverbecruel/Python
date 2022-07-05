cont = fator = result = 1
while True:
    print('-' * 30)
    tab = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if tab < 0:
        break
    for c in range(1, 11):
        print(f'{tab} x {c} = {tab * c}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')



        # result = cont * tab
