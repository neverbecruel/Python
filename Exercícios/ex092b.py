from datetime import datetime

class Pessoa():
    def __init__(self):
        self.nome = None
        self.ano_de_nasc = None
        self.CTPS = None
        self.contratdat = None
        self.salario = None
        
    def info(self):
        self.nome = input('Nome: ')
        self.ano_de_nasc = int(input('Ano de nascimento: '))
        idade = datetime.now().year - self.ano_de_nasc
        self.CTPS = int(input('Carteira de trabalho: (Digite 0 se não tiver.) '))
        if self.CTPS != 0 and self.CTPS != None:
            self.contratdat = int(input('Ano de contratação: '))
            iddcontrat = self.contratdat - self.ano_de_nasc
            self.salario = float(input('Salário: '))
        print('=-' * 30)
        print(f'Seu nome é: {self.nome}.')
        print(f'Você tem {idade} anos.')
        if self.CTPS != 0 and self.CTPS != None:
            print(f'Seu CTPS é: {self.CTPS}.')
            print(f'Você foi contratado em {self.contratdat}.')
            print(f'Seu salário é de R${self.salario:.2f}.')
            print(f'Você vai se aposentar aos {iddcontrat + 35}')
            
pessoa = Pessoa()
pessoa.info()
                                  
