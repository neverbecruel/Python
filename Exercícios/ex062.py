t1 = int(input('Digite o primeiro termo da P.A. '))
razao = int(input('Digite a razão da P.A. '))
cont = 1
print(t1, end=' -> ')
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont < total:
        t1 += razao
        print(t1, end=' -> ')
        cont += 1
    print('PAUSA')
    mais = (int(input('Quantos termos a mais você quer mostrar? ')))
print(f'Progressão finalizada com {total} termos mostrados. ')



