class Tamagushi:
    def __init__(self, Nome, Fome = 10, Saude = 0, Idade = 1):
        self.Nome = Nome
        self.Fome = Fome
        self.Saude = Saude
        self.Idade = Idade

    def alt_Nome(self, Nome):
        self.Nome = Nome

    def alt_Fome(self, Fome):
        self.Fome = Fome

    def alt_Saude(self, Saude):
        self.Saude = Saude
        
    def alt_Idade(self, Idade):
        self.Idade = Idade

    def CheckHumor(self): 
        if self.Fome > 7 or self.Saude <= 3:
            return 'está mal-humorado'
        else:
            return 'está de bom humor'
            
    def DarComida(self, Quantidade):
        if (Quantidade >= 0) and (Quantidade <= 100):
            self.Fome -= self.Fome * (Quantidade / 100.0)

    def brincar(self, Quantidade):
        if (Quantidade >= 0) and (Quantidade <= 100):
            self.Saude += self.Saude * (Quantidade / 100.0)
            
sol = Tamagushi('VALERIA')
sol.alt_Nome('LISS')
sol.alt_Fome(9)
sol.alt_Saude(5)
sol.alt_Idade(10)
sol.DarComida(50)
sol.brincar(8)

print('Nome:',sol.Nome)
print(sol.Fome,'de fome')
print(sol.Saude,'de saúde')
print(sol.Idade,'anos')
print('O bichinho',sol.CheckHumor())