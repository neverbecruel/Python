class MaiorReta(object):
    def __init__(self, reta1, reta2, reta3):
        self.reta1 = reta1
        self.reta2 = reta2
        self.reta3 = reta3
        
    def maior(self):
        maior = self.reta1
        if self.reta2 > maior:
            maior = self.reta2
        if self.reta3 > maior:
            maior = self.reta3
        print(f'A maior reta, mede: {maior}')
        
    def is_triang(self):
        if self.reta1 + self.reta2 >= self.reta3:
            print('É possivel fazer um triangulo com essas retas...')
    

reta1 = int(input("Digite o valor da primeira reta: "))
reta2 = int(input("Digite o valor da segunda reta: "))
reta3 = int(input("Digite o valor da terceira reta: "))


maior_reta = MaiorReta(reta1, reta2, reta3)
maior_reta.maior()
maior_reta.is_triang()