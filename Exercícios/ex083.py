expressao = input('Digite a expresão: ')
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            break
if pilha == 0:
    print('Expressão válida. ')
else:
    print('Expressão inválida. ')