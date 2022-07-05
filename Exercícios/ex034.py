s= int(input('qual é o valor do seu salario? '))
a1 = s+(s/10)
a2 = s+(15/100*s)
if s <= 1250:
    print('o seu salario com o aumento de 15% será de {}'.format(a2))
else:
    print('o seu salário com o aumento de 10% será de {}'.format(a1))