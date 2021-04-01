coluna=0
i=0
linha=0
j=0

lar = int(input("Digite a largura: "))
alt = int(input("Digite a altura : "))


while(alt > linha):
    while(lar > coluna):
            print('#', end = "")
            coluna = coluna + 1
    print()
    linha = linha + 1
    coluna = 0


   
    
