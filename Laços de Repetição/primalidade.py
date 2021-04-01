x = int(input("Digite um número inteiro: "))
i = 1
y = 0
z = 0

while(i <= x):
    if x % i == 0:
        y=y+1
    i=i+1

if(y > 2):
    print("não primo")
else:
    print("primo")
