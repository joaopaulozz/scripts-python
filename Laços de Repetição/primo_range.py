a = int(input(""))
resto=0

for x in range(1, a+1):
    if a % x == 0:
        resto += 1

if resto == 2:      
    print("N° {} É PRIMO".format(a))
else:
    print("N° {} NÃO É PRIMO".format(a))
