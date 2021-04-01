def maior_primo(p):
    while p >= 2:
        i = p - 1
        p % 1 == 0
        return p


def éPrimo(k):
    i = 2
    é_primo = 0
    while i < k:
        if k % i ==0:
            break
        else:
            i = i+1
    if i == k:
        é_primo = False
        return False
    else:
        é_primo = True
        return True
