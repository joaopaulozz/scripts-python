def sao_multiplicaveis(m1,m2):
    coluna = len(m1)
    coluna2 = len(m2)
    linha = 1
    linha2 = 1
    for i in m1:
        linha = len(i)

    for j in m2:
        linha2 = len(i)

    if coluna == linha2:
        return True
    else:
        return False

m1 = [[1, 1], [1, 1]]
m2 = [[2],[2]]
