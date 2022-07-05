from datetime import datetime
pessoa = {}
pessoa['nome'] = input('Nome: ')
ano_de_nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - ano_de_nascimento
carteira_de_trabalho = int(input('Carteira de trabalho: (Digite 0 de não tiver.) '))
if carteira_de_trabalho != 0:
    pessoa['CTPS'] = carteira_de_trabalho
    pessoa['ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: $'))
    idade_quando_contratado = pessoa['ano de contratação'] - ano_de_nascimento
    pessoa['aposentadoria'] = idade_quando_contratado + 35
print('=-' * 30)
# podia ser feito do seguinte jeito, mas achei feio
'''for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')'''

# então fiz assim:

print(f'Seu nome é: {pessoa["nome"]}.')
print(f'Você tem {pessoa["idade"]} anos.')
if carteira_de_trabalho != 0:
    print(f'Sua CTPS é: {pessoa["CTPS"]}.')
    print(f'Você foi contrtado em {pessoa["ano de contratação"]}.')
    print(f'Seu salário é de R${pessoa["salario"]:.2f}.')
    print(f'Vai se aposentar aos {pessoa["aposentadoria"]}.')

