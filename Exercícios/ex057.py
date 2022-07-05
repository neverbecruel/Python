sexo = str(input('Informe seu sexo: [F/M] ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dado inválido. Por favor, digite novamente:  ')).upper().strip()[0]
print('sexo {} validado com sucesso.'.format(sexo))
