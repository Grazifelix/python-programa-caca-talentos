# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
# Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
# com valor default zero e os demais atributos são obrigatórios.
# Graziela Felix
# 05/04/23

class ContaCorrente:
    def __init__(self, numeroDaConta, nomeCorrentista, saldo=0):
        self.numeroDaConta = numeroDaConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def alterarnome(self, novoNome):
        self.nomeCorrentista = novoNome

    def deposito(self, valorDeposito):
        self.saldo += valorDeposito

    def saque(self, valorSaque):
        self.saldo -= valorSaque

    def extrato(self):
        print("\n======EXTRATO======")
        print(f"Numero da conta:{self.numeroDaConta}\nNome: {self.nomeCorrentista}\nSaldo: {self.saldo}")


if __name__ == '__main__':
    conta = ContaCorrente(3322, "João Miguel")
    conta.extrato()

    conta.deposito(500)
    conta.extrato()

    conta.saque(55)
    conta.extrato()

