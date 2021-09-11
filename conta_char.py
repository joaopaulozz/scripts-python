
frase = 'programamos em python'

def conta_letras(frase, contar=""):
    if contar == 'vogais':
        contar = 'aeiou'
    elif contar == 'consoantes':
        contar = 'bcdfghjklmnpqrstvxywz'
    elif contar == '':
        contar = 'aeiou'
    i = 0
    j = 0
    r = 0
    for x in frase:
        j = 0
        for y in contar:
            if contar[j] == frase[i]:
                r = r + 1
            j = j + 1
        i = i + 1

    return r

