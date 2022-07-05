from datetime import date
ano = int(input('em que ano voce nasceu? '))
idade = date.today().year - ano
if idade <= 9:
    print('voce entra na classificação MIRIM')
elif idade > 9 and idade < 15:
    print('voce entra na classificação INFANTIL')
elif idade >= 15 and idade < 19:
    print('voce entra na classificação JUNIOR')
elif idade == 20:
    print('voce entra na classificação SÊNIOR')
elif idade > 20:
    print('voce entra na classificação MASTER')