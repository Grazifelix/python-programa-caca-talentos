# crie uma classe pessoa, diretor, professor e aluno e utilize os principios de Herança
# Graziela Felix
# 28/11/22

class Pessoa:
    def __init__(self, pnome, psobrenome):
        self.pnome = pnome
        self.psobrenome = psobrenome

    def printp(self):
        print(self.pnome, self.psobrenome)


class Diretor(Pessoa):
    pass  # pass é usado quando não se quer atribuir novos metodos e atributos a class filha


class Professor(Pessoa):
    def __init__(self, pnome, psobrenome):
        Pessoa.__init__(self, pnome, psobrenome)
        # chama a função init da classe mãe,
        # se não fosse atribuido
        # a classe não herdaria o init da classe mãe


class Aluno(Pessoa):
    def __init__(self, pnome, psobrenome, ano):
        super().__init__(pnome, psobrenome)
        # fará com que a classe filha herde todos os métodos e
        # atributos da sua mãe: O super() é utilizado entre
        # heranças de classes, ele nos proporciona extender/subscrever
        # métodos de uma super classe (classe pai) para uma sub classe (classe filha),
        # atrávez dele definimos um novo comportamento para um determinado método
        # construido na classe pai e herdado pela classe filha.
        self.anodeconclusao = ano

    def printp(self):
        print(f"{self.pnome} {self.psobrenome} | {self.anodeconclusao}")  # Polimorfismo e Redefinição de Método


p = Professor('Juju', "Viera")
p.printp()  # Polimorfismo

p1 = Diretor('Joao', "Claudio")
p1.printp()  # Polimorfismo

a = Aluno("Romano", "Tiago", 2022)
a.printp()  # Polimorfismo
