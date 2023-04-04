# Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor
# 11/12/22

class Bola:
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def troca_cor(self, nova_cor):
        self.cor = nova_cor

    def mostra_cor(self):
        print(f'A cor da bola é: {self.cor}')

    def __str__(self):
        return f'--*Propriedades da bola*--\n Cor: {self.cor}\n Circuferencia: {self.circuferencia}\n Material: {self.material}'


bola = Bola('Azul', 34, 'Couro')
bola.mostra_cor()
bola.troca_cor('Verde')
bola.mostra_cor()
print(bola)