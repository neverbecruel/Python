def area(largura, comprimento):
    return largura * comprimento

print('controle de terreno:')
print('--' * 10)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
print(f'A área do terreno é de {area(largura, comprimento):.1f}m²')