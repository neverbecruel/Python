from datetime import date
dia =  int(input('em que dia você nasceu? '))
mes = int(input('em que mes voce nasceu? '))
ano = int(input('em que ano voce nasceu? '))
atual = date.today().year
if atual - ano < 18:
    print('daqui a {} anos voce vai se alistar no exercito'.format(18 - (atual - ano)))
elif atual- ano > 18:
    print('voce devia ter se alistado ha {} anos'.format((atual - ano) - 18))
elif atual - ano == 18:
    print('esta na hora de voce se alistar no exercito')