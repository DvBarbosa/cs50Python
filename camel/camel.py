# Solicita o nome da variável em camel case ao usuário
nome_camel_case = input("Digite o nome da variável em Camel Case: ")
# Converte o nome para snake case
nome_snake_case = ""
for i in range(len(nome_camel_case)):
    if nome_camel_case[i].isupper() and i > 0:
        nome_snake_case += "_"
    nome_snake_case += nome_camel_case[i].lower()

# Imprime o nome da variável em snake case
print("O nome da variável em Snake Case é:", nome_snake_case)
