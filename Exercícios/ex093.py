jogador = {}
gols_lista = []


def linha_bnt():
    print('-=' * 30)


jogador['nome'] = input('Nome do jogador: ')
numero_de_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(numero_de_partidas):
    gols_lista.append(int(input(f'Quantos gols na {c+1}ª partida: ')))
tota_de_gols = sum(gols_lista)
jogador['gols'] = gols_lista[:]
jogador['total'] = tota_de_gols
linha_bnt()
print(jogador)
linha_bnt()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
linha_bnt()
print(f'O jogador {jogador["nome"]} jogou {numero_de_partidas}.')
for x in range(numero_de_partidas):
    print(f'=> Na partida {x+1}, fez {jogador["gols"][x]}')
print(f'Foi um total de {tota_de_gols} gols')
print()
linha_bnt()
