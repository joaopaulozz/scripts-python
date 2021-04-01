n=1
i=0
while(n>=i):
    n = int(input("Digite um número: "))
    fat = 1
    while(n>1):
        fat = fat * n
        n = n - 1
    print(fat)
    i = i + 1
    
