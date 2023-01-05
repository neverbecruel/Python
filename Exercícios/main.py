class Soma(object):
    def __init__(self,):
        self.num1 = None
        self.num2 = None
        
    def soma(self):
        return self.num1 + self.num2
    


soma = Soma()
soma.num1 = int(input('Digite um numero para a soma: '))
soma.num2 = int(input('Digite outro numero para a soma: '))
print(soma.soma())