import sys

# Solicita que o usuário informe os nomes
print("Informe os nomes. Pressione Ctrl-D quando terminar.")
nomes = []
while True:
    try:
        entrada = input("Nome: ")
        nomes.append(entrada)
    except EOFError:
        break

# Diz adeus aos nomes informados
quantidade_nomes = len(nomes)
if quantidade_nomes == 1:
    print(f"Adieu, adieu, to {nomes[0]}")
elif quantidade_nomes == 2:
    print(f"Adieu, adieu, to {nomes[0]} and {nomes[1]}")
else:
    # Para três ou mais nomes, use vírgulas e um "and"
    nomes[-1] = f"and {nomes[-1]}"
    if quantidade_nomes == 3:
        print(f"Adieu, adieu, to {' '.join(nomes)}")
    else:
        print(f"Adieu, adieu, to {', '.join(nomes[:-1])}, {nomes[-1]}")

