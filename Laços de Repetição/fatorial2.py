num = int(input("Digite um numero para calcular seu fatorial: "))
fat = 1
resu=num
while (num > 0):
    fat = fat * num
    num = num - 1

print("Fatorial de",resu,"!","é",fat)

input()
