# Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer.
# Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
# Graziela Felix
# 04/04/23

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.05

    def engordar(self, quilos_ganhos):
        self.peso += quilos_ganhos

    def emagrecer(self, quilos_perdidos):
        self.peso -= quilos_perdidos

    def crescer(self, centimetros):
        self.altura += centimetros/100

    def __str__(self):
        return f"=====PESSOA=====\nNome: {self.nome}\nIdade: {self.idade}\nAltura: {self.altura:.2f}cm\nPeso: {self.peso}"


pessoa = Pessoa("Julia", 18, 46, 1.60)
print(pessoa)

pessoa.engordar(2)
pessoa.envelhecer()
print(pessoa)

pessoa.crescer(5)
pessoa.emagrecer(5)
pessoa.envelhecer()
print(pessoa)

pessoa.envelhecer()
print(pessoa)
