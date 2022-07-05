tab = int(input('deseja saber a tabuada de qual numero? '))
cont = 0
for c in range(tab, tab * 10 + 1, tab):
    cont = cont + 1
    print('{} {} {} {} {}'.format(tab, 'x', cont, '=', c))