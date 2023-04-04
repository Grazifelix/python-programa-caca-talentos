# Itere em uma classe usando as funções iter() e next()
# Graziela Felix
# 28/11/22

class MeusNumeros:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += x
        return x

minhaclasse = MeusNumeros()
meuiter = iter(minhaclasse)
print(next(meuiter))
print(next(meuiter))
print(next(meuiter))
print(next(meuiter))
print(next(meuiter))

