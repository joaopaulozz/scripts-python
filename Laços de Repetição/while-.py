num = int(input("Digite quantos números voce quer somar:"))

i=0
soma=0

while(i < num):
    n= int(input(" - "))
    soma = soma + n
    num = num - 1

print("",soma)
