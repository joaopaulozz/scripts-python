import math

x1 = int(input("Digite um numero: "))
y1 = int(input("Digite um numero: "))
x2 = int(input("Digite um numero: "))
y2 = int(input("Digite um numero: "))

teo = x1 - x2
teor = y1 - y2

n11 = pow(teo,2)
           
n22 = pow(teor,2)

a2 = n11 + n22 

raiz = math.sqrt(a2)

if raiz >= 10:
    print("longe",raiz)

else:
    print("perto",raiz)


