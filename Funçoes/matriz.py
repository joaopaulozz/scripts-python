def matriz(n_linhas, n_colunas, valor):

    matriz = [] #cria lista vazia
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            linha.append(valor)
            
        matriz.append(linha)

    return matriz
