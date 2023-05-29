def main():
  #inicia um dicionario vazio para armazenar os itens e contar
    items = {}

    # mantenha fazendo prompt do usuario com os itens até pressionar control-d
    while True:
        try:
            item = input().strip().lower()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
        except EOFError:
            break

    # organize os itens de forma alfabetica
    sorted_items = sorted(items)

    #imprima a contagem dos itens com o nome de cada um no dicionario
    for item in sorted_items:
        count = items[item]
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
