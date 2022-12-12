# Classe Retangulo: Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe.
# Ele deve pedir ao usuário que informe as medidades de um local.
# Depois, deve criar um objeto com as medidas e calcular a
# quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def get_perimetro(self):
        return int(self.base*2+self.altura*2)

    def get_area(self):
        return int(self.base*self.altura)

    def show_base(self):
        return int(self.base)

    def show_altura(self):
        return int(self.altura)

    def change_base(self, new_base_value):
        self.base = new_base_value

    def change_altura(self, new_altura_value):
        self.altura = new_altura_value

    def __str__(self):
        return f"Retangulo\n Base: {self.base}\n Altura: {self.altura}\n Perimetro: {self.get_perimetro()}\n Area: {self.get_area()}"


retangulo = Retangulo(12, 20)
print(retangulo)
retangulo.change_base(20)
retangulo.change_altura(40)
retangulo.show_base()
retangulo.show_altura()

def print_piso(local, piso):
    # quantidade de pisos para o local
    print(
        f"A quantidade de pisos para o local é: {local.get_area() / piso.get_area()} de {piso.show_base()}x{piso.show_altura()}")

def print_rodape(local, rodape):
    # quantidade de rodapes para o local
    print(f'Quantidade de rodapes: {local.get_perimetro() / rodape.base} de {rodape.show_base()}x{rodape.show_altura()}')


if __name__ == "__main__":
    print("== CALCULADORA DE PISOS E RODAPÉS ==")

    # local
    base = float(input('Valor do comprimento do local: '))
    altura = float(input('Valor da largura do local: '))
    local = Retangulo(base, altura)

    # Piso
    base_piso = float(input('Valor do comprimento do piso: '))
    altura_piso = float(input('Valor da largura do piso: '))
    piso = Retangulo(base_piso, altura_piso)

    # rodape
    base_rodape = float(input("valor do comprimento do rodape: "))
    altura_rodape = float(input("valor da largura do rodape: "))
    rodape = Retangulo(base_rodape, altura_rodape)

    print_piso(local, piso)
    print_rodape(local, rodape)


while True:
    print("Deseja alterar medidas do local, piso e/ou rodape? [s/n]")
    res = input()
    if res == 'n':

        break

    print('Deseja mudar as medidas do local? [s/n]')
    option = input()
    if option == 's':
        base = float(input('medida: '))
        local.change_base(base)
        altura = float(input('medida: '))
        local.change_altura(altura)
    else:
        pass

    print('Deseja mudar as medidas do piso? [s/n]')
    option = input()
    if option == 's':
        base = float(input('medida: '))
        piso.change_base(base)
        altura = float(input('medida: '))
        piso.change_altura(altura)
    else:
        pass

    print('Deseja mudar as medidas do rodape? [s/n]')
    option = input()
    if option == 's':
        base = float(input('medida: '))
        rodape.change_base(base)
        altura = float(input('medida: '))
        rodape.change_altura(altura)
    else:
        pass

    print_piso(local, piso)
    print_rodape(local, rodape)
