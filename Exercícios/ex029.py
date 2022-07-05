v= int(input('qual a velocidade do carro? '))
m= (v-80)*7

if v > 80:
    print('você excedeu o limite de velocidade que é de 80Km/h,sua multa é de R${},00'.format(m))
else:
    print('tudo bem, pode continuar')