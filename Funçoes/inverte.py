l=[]
x=1

while x != '0':
    x=input("Digite um número: ")
    if x == '0':
        break
    else:
        l.append(x)

print()
l.reverse()

for i in l:
    print(i)


