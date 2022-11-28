# Crie uma classe Pessoa que tenha nome e idade, que tenha um método que retorne as informações
# Graziela Felix
# 28/11/22

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_info(self):
        print(f"{self.nome}: {self.idade}")


p1 = Pessoa("Julia", 12)
p1.mostrar_info()
