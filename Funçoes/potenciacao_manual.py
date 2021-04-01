base = int(input("Digite a base:"))
exp = int(input("Digite o expoente:"))
i=0
res=1

while(i<exp):
    if(exp==0):
        res=1
    res = base*res
    i = i + 1

print("",res)

input()
