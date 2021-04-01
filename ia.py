import random

def ag (precind,qind):

    if precind % 2 ==0 and qind % 2 == 0:
        j=0
        i=0
        while(j < precind):
            while(i < qind):
                i=i+1
                print(random.randint(0, 1),end="")
            print("")
            i=0
            j=j+1

    else:
        return "Dados invalidos, só é permitido número pares"
