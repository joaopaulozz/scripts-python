def maximo(a,b,c):
    if (a > b and b > c):
        return a
    
    if (b > a and a > c):
        return b

    else:
        return c
