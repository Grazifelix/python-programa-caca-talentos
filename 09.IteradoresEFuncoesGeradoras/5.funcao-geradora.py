# Função geradora usando Yield
# Graziela Felix
# 28/11/22

def quadrados():
    i=1
    while True:
        yield i*i
        i += 1


for num in quadrados():
    if num > 100:
        break
    print(num)
