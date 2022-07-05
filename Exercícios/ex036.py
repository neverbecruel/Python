valor = float(input('qual o valor da casa em reais? R$'))
salario = float(input('qual a sua renda mensal? R$'))
tempo = float(input('em quantos anos pretende quitar a casa? '))
parcel = valor / (tempo * 12)
porc = salario / 10 * 3
if parcel < porc:
    print('Emprestimo pode ser CONCEDIDO.')
else:
    print('Empréstimo NEGADO.')

