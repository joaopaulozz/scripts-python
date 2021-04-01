# Poderia ser um input("Digite o nome do arquivo: ")
nome = "poesia.txt" 

with open(nome, 'r', encoding='utf-8') as arq_entrada:
    conteudo = arq_entrada.read()

print(conteudo)
