import datetime


def voto(ano):
    if idade < 18:
        return 'VOTO NEGADO'
    elif idade >= 18 and idade < 65:
        return 'VOTO OBRIGATÓRIO'
    elif idade > 65:
        return 'VOTO OPCIONAL'


ano = int(input('Em que ano você nasceu? '))
atual = datetime.datetime.now().year
idade = atual - ano
print(f'A idade atual é: {idade}, {voto(ano)}')