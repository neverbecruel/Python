a = b = c = 0
while True:
    print('~~' * 16)
    print('       CADASTRE UMA PESSOA')
    print('~~' * 16)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mMfF':
        sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
    if idade >= 18:
        a += 1
    if sexo == 'm':
        b += 1
    if sexo in 'Ff' and idade < 20:
        c += 1
    play = ' '
    while play not in 'SsnN':
        play = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if play in 'n':
        print('~~' * 16)
        break
print(f'Total de pessoas com mais de 18 anos: {a} \nAo todo, temos {b} homens cadastrados \nE temos {c} mulheres com '
      f'menos de 20 anos')
