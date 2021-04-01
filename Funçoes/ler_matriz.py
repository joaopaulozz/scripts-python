def matriz(n_linhas, n_colunas):

    matriz = [] #cria lista vazia
    for i in range(n_linhas):
        linha = []  # cria as linhas
        for j in range(n_colunas):
            valor = int(input("Digite o elemento[" + str(i) + "][" + str(j) +"] ",end=""))
            linha.append(valor) # cria as colunas da linha
            
        matriz.append(linha) # adiciona na matriz as linhas

    return matriz


def ler():
    lin = int(input("Digite o n de linhas da matriz "))
    col = int(input("Digite o n de colunas da matriz "))

    return matriz(lin,col)
