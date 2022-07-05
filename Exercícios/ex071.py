contcin = contvint = contdez = contum = 0
while True:
    print('==' * 16)
    print('          BANCO CEV')
    print('==' * 16)
    valor = float(input('Qual valor você quer sacar? R$'))
    quant = valor
    while valor >= 50:
        valor -= 50
        contcin += 1
    while valor < 50 and valor > 20:
        valor -= 20
        contvint += 1
    while valor < 20 and valor > 10:
        valor -= 10
        contdez += 1
    while valor < 10 and valor > 0:
        valor -= 1
        contum += 1
    if contcin >= 1:
        print(f'Total de {contcin} de R$50,00')
    if contvint >= 1:
        print(f'Total de {contvint} de R$20,00')
    if contdez >= 1:
        print(f'Total de {contdez} de R$10,00')
    if contum >=1:
        print(f'Total de {contum} de R$1,00')
    break
#print(f'Você sacou {quant:.2f} ')
print('==' * 16)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')