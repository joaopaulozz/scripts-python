idade_pessoas = {
    'Ana' : 7,
    'Jose' : 38,
    'Paulo' : 22,
    'Lucia' : 59,
    'Cristina' : 44,
    'Luiz' : 12
    }

maiores_idade = []
menores_idade = []

while len(idade_pessoas) > 0:
    pessoas = list(idade_pessoas.keys())
    pessoa = pessoas[0]

    if idade_pessoas[pessoa] >= 18:
        maiores_idade.append(pessoa)
    else:
        menores_idade.append(pessoa)

    del idade_pessoas[pessoa]

print(maiores_idade)
print(menores_idade)
    
