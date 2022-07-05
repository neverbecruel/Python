dicionario = {}
dicionario['nome'] = str(input('Nome: '))
dicionario['media'] = float(input('Média: '))
print(f'O nome é {dicionario["nome"]}')
if dicionario['media'] >= 7:
    print(f'{dicionario["nome"]} está APROVADO.')
elif dicionario['media'] < 7 and dicionario['media'] >= 5:
    print(f'{dicionario["nome"]} ficou de RECUPERAÇÃO.')
elif dicionario['media'] < 5:
    print('{} está REPROVADO.'.format(dicionario['nome']))


