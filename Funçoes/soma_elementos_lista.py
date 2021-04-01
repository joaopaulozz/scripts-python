def soma_elementos(lista):
    soma=0
    for i in lista:
        soma = i + soma
    return soma
    
lista = [1,2,3]
print(soma_elementos(lista))
