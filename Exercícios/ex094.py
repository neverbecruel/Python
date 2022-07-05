todo_mundo = []
pessoa = {}
soma_das_idades = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ').capitalize()
    pessoa['idade'] = int(input('Idade: '))
    soma_das_idades += pessoa['idade']
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas F ou M ')
    todo_mundo.append(pessoa.copy())
    while True:
        resp = str(input('Quer cadastrar mais alguém: ')).strip().lower()[0]
        if resp in 'ns':
            break
    if resp == 'n':
        break
media = soma_das_idades / len(todo_mundo)
print('-=' * 30)
print(f'A) Ao todo, temos {len(todo_mundo)} cadastradas')
print(f'B) A média entre a idades é {media:.2f}.')
print(f'C) As mulheres cadastradas foram: ', end='')
for c in todo_mundo:
    if c['sexo'] == 'F':
        print(f'{c["nome"]} ', end='')
print()
print(f'D) Lista das pessoas com idade acima da média: ', end='')
for x in todo_mundo:
    if x['idade'] > media:
        print(f'{x["nome"]} ', end='')
print()
print('-=' * 30)
