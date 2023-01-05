class Caixa(object):
    def __init__(self, valor_sac):
        self.valor_sacT = valor_sac
        self.valor_sac = valor_sac
        self.notcinqu = 0
        self.notvint = 0
        self.notdez = 0
        self.notum = 0
        
             
    def qtd_notas(self):
        while self.valor_sac >= 50:
            self.valor_sac -= 50
            self.notcinqu += 1       
        while self.valor_sac < 50 and self.valor_sac > 20:
            self.valor_sac -= 20
            self.notvint += 1
        while self.valor_sac < 20 and self.valor_sac > 10:
            self.valor_sac -= 10
            self.notdez += 1           
        while self.valor_sac < 10 and self.valor_sac > 0:
            self.valor_sac -= 1
            self.notum += 1
        print('Será necessário: ')
        if self.notcinqu >= 1:
            print(f'    {self.notcinqu} notas de R$50,00')
        if self.notvint >= 1:
            print(f'    {self.notvin} notas de R$20,00')
        if self.notdez >= 1:
            print(f'    {self.notdez} notas de R$10,00')
        if self.notum >= 1:
            print(f'    {self.notum} notas de R$1,00')
        print('==' * 16)
        print('   VOLTE SEMPRE AO BANCO C.E.V.')
          
             
caixa = Caixa(input('Quanto Você quer sacar? '))
caixa.qtd_notas()