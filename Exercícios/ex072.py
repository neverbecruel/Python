tupla = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')
while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    while escolha > 20 or escolha < 0:
        escolha = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {tupla[escolha]}')
    resp = ' '
    while resp not in 'SsnN':
        resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp == 'n':
        break
print('PROGRAMA ENCERRADO. Volte sempre! ')

# print(f'Você digitou o número {tupla[escolha]}')
