jogadores = list()
jogador = dict()
gols_lista = []


def linha_bnt():
    print('-=' * 30)


while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ').capitalize()
    numero_de_partidas = int(input(f'  Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(numero_de_partidas):
        gols_lista.append(int(input(f'  Quantos gol {jogador["nome"]} fez na {c + 1}ª partida: ')))
    jogador['gols'] = gols_lista[:]
    total_de_gols = sum(gols_lista)
    jogador['total'] = total_de_gols
    gols_lista.clear()
    jogadores.append(jogador.copy())
    resp = input(' Quer continuar? [S/N] ').lower().strip()[0]
    while resp not in 'ns':
        resp = input(' Quer continuar? [S/N] ').lower().strip()[0]
    if resp == 'n':
        break
linha_bnt()
print(f'cod ', end='')
for w in jogador.keys():
    print(f'{w:<20}', end='')
print()
print('-'*60)
for i in range(0, len(jogadores)):
    print(f'{i:^3} {jogadores[i]["nome"]:<17}   {str(jogadores[i]["gols"]):<20}{jogadores[i]["total"]:<3}')
linha_bnt()
while True:
    qual_jogador = int(input("Digite o 'cod' do jogador para mais detalhes: (999 para encerrar) "))
    if qual_jogador == 999:
        break
    if qual_jogador >= len(jogadores):
        print('Jogador não encontrado! Tente novamente...')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {jogadores[qual_jogador]["nome"]}')
        linha_bnt()
        for k in range(len(jogadores[qual_jogador]['gols'])):
            print(f'No jogo {k+1}, fez {jogadores[qual_jogador]["gols"][k]} gols')
        linha_bnt()
print('<<< VOLTE SEMPRE >>>')
