f = str(input('digite uma frase: ')).lower().strip()
print('a frase que você digitou foi:{}'.format(f))
print('nessa frase a letra a aparece {} vezes'.format(f.count('a')))
print('a letra a aparece pela primeira vez nessa frase na posição {}'.format(f.find('a') + 1))
print('a letra a aparece pela ultima vez na posação {}'.format(f.rfind('a') + 1))
