r1= float(input('digite o comprimento da 1a reta: '))
r2= float(input('digite o comprimento da 2a reta: '))
r3= float(input('digite o comprimento da 3a reta: '))

#descobrindo o maior
maior = r1
if r2 > maior:
    maior = r2
if r3 > maior:
    maior = r3

if r1+r2 >= r3:
    print('Com essas retas é possivel formar um triangulo.')
else:
    print('Com essas retas não é possivel formar um triangulo')