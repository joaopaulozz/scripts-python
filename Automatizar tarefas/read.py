nome = "poesia.txt" # poderia ser um input("Digite o nome do arquivo com sua extensão: ")

with open(nome, 'w', encoding='utf-8') as arq:
    arq.write("Bem vindo ao meu mundo!!\n")
