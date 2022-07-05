v = int(input('qual a distancia em KM da sua viagem? '))
v1 = 0.50*v
v2 =0.45*v
if v <= 200:
    print('sua viagem custará R${}0'.format(v1))
else:
    print('sua viagem custará RS{}0'.format(v2))