palavras = (
    'APRENDER', 'PROGRAMAS', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
    'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRMADOR', 'FUTURO'
            )
for p in palavras:
    print(f'\nNa palavra {p}, temos: ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end='')

