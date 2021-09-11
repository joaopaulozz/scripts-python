
frase = 'PrOgRaMaMoS em python!'

def maiusculas(frase):
    i = 0
    a = 0
    m = ''

    for x in frase:
        #print(texto[i])
        if frase[i].isupper():
            m = m + frase[i]
        i = i + 1

    return(m)
