# Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        self.area = 0
        self.lado = lado

    def change_side_value(self, new_side_value):
        self.lado = new_side_value

    def return_side_valeu(self):
        print(self.lado)

    def calc_area(self):
        self.area = self.lado*2

    def __str__(self):
        return f"Quadrado\n Lado: {self.lado}\n Area: {self.area}"


quadrado = Quadrado(25)
quadrado.return_side_valeu()
quadrado.change_side_value(30)
quadrado.calc_area()
print(quadrado)
