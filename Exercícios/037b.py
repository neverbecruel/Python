class Conversor(object):
    def __init__(self):
        self.num = None
        
    def operacao(self):
        self.num = int(input("Digite o número que quer converter:\n> "))
        #print(self.num)
        print(f'Quer converter {self.num} para: ')
        print('BINARIO [1] ')
        print('OCTAL [2] ')
        print('HEXADECIMAL [3] ')
        opcao = input("> ")
        if opcao == '1':
            print(f'{self.num} em BINÁRIO = {bin(self.num)[2:]}')
        if opcao == '2':
            print(f'{self.num} em OCTAL = {oct(self.num)[2:]}')
        if opcao == '3':
            print(f'{self.num} em HEXADECIMAL = {hex(self.num)[2:]}')
            
            
            
converter = Conversor()
converter.operacao()