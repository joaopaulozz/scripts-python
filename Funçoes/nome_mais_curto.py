
def mais_curto(lista):
    menor = min(lista, key=lambda x: len(x.strip()))
    return (menor.strip())


lista = ["joao", "enzo", "pedro", "danilo", "vitor", "wellington"]
print(mais_curto(lista))

