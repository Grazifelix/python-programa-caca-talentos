# Usando Yield
# Graziela Felix
# 28/11/22

def gerador_simples():
    yield 1
    yield 2
    yield 3

for x in gerador_simples():
    print(x)