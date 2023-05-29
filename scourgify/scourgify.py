import sys
import csv

def main():
    """
    Lê um arquivo CSV com nomes no formato "sobrenome, nome" e cria um novo arquivo CSV com os nomes no formato "nome,sobrenome".
    """
    # Verifica se os argumentos foram passados corretamente
    check_command_line_arg()

    # Armazena os dados do arquivo original em uma lista de dicionários
    data = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Separa o nome e sobrenome
                name_parts = row['name'].split(",")
                # Armazena os dados em um novo dicionário
                new_row = {"first": name_parts[1].lstrip(), "last": name_parts[0], "house": row['house']}
                data.append(new_row)
    except FileNotFoundError:
        sys.exit("Could not read {}".format(sys.argv[1]))

    # Escreve os dados no novo arquivo CSV
    try:
        with open(sys.argv[2], "w") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except IOError:
        sys.exit("Could not write to {}".format(sys.argv[2]))

def check_command_line_arg():
    """
    Verifica se os argumentos foram passados corretamente e se os arquivos possuem a extensão .csv.
    """
    # Verifica o número de argumentos
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 {} input.csv output.csv".format(sys.argv[0]))

    # Verifica a extensão dos arquivos
    if not check_extension(sys.argv[1]) or not check_extension(sys.argv[2]):
        sys.exit("Not a CSV file")

def check_extension(filename):
    """
    Verifica se o arquivo tem a extensão .csv.
    """
    return filename.lower().endswith('.csv')

if __name__ == "__main__":
    main()

