import sys
import csv
from tabulate import tabulate

def main(filename):
    check_command_line_arg(filename)
    # Cria uma variavel para armazenar os arquivos da tabela
    table = []
    #tente abrir o arquivo
    try:
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)
    # Se não for possivel abrir, significa que o arquivo nao existe
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(table[1:], table[0], tablefmt="grid"))

def check_command_line_arg(filename):
    #check se é um arquivo CSV
    if not filename.endswith('.csv'):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py filename.csv")
    main(sys.argv[1])
