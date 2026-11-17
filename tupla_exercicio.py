'''
Exercício: tuplas, listas e dicionários
'''

# 1. Crie uma tupla com 5 dados
cores = ("Azul", "Verde", "Vermelho", "Amarelo", "Preto")
print("Tupla:", cores)

# 2. Altere a tupla para uma lista
cores_lista = list(cores)
print("Lista:", cores_lista)

# 3. Insira 2 dados extras a essa lista
cores_lista.append("Branco")
cores_lista.append("Roxo")
print("Com 2 dados extras:", cores_lista)

# 4. Remova o primeiro dado da lista
cores_lista.pop(0)
print("Sem o primeiro:", cores_lista)

# 5. Remova o último dado da lista
cores_lista.pop()
print("Sem o último:", cores_lista)

# 6. Faça um print com o primeiro dado da lista
print("Primeiro dado:", cores_lista[0])

# 7. Faça um print com a quantidade de dados da lista
print("Quantidade de dados:", len(cores_lista))

print(20 * "-")

# 8. Crie um dicionário com os dados: Nome, Idade, Profissão
pessoa = {
    "nome": "Caio",
    "idade": 30,
    "profissao": "Analista de QA"
}

# 9. Imprima somente o valor contido na chave Nome do dicionário
print("Nome:", pessoa["nome"])
