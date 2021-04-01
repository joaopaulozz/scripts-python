import math

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

delta = (b**2) - (4 * a * c)

if delta == 0:
    x1 = (- b + math.sqrt(delta)) / (2*a)
    print("a raiz desta equação é",x1)
        
else:
    if delta < 0 :
        print("esta equação não possui raízes reais")
    else:
        x1 = (- b + math.sqrt(delta)) / (2*a)
        x2 = (- b - math.sqrt(delta)) / (2*a)
        
        print("as raízes da equação são",x1,"e",x2)

       
