class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, percentualDeAumento):
        self.salario += self.salario * (percentualDeAumento / 100.0)
        

luis = Funcionario("LUIS", 25000)
luis.aumentarSalario(10)
print (f'Nome: {luis.getNome()}')
print (f'Salario: R$ {luis.getSalario():.2f}')