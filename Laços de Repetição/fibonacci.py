x = int(input("Digite um número: "))
anterior = 0
proximo = 0

while(proximo < x):
    print(proximo, end=" - ")
    proximo = proximo + anterior
    anterior = proximo - anterior
    
    if(proximo == 0):
        proximo = proximo + 1
        
