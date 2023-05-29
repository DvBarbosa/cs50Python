import sys

def main():
    # Verifica se os argumentos da linha de comando estão corretos
    check_command_line_args()

    # Tenta abrir o arquivo
    try:
        with open(sys.argv[1], "r") as file:
            file_lines = file.readlines()
        file.close()
    # Se não conseguir abrir, significa que o arquivo não existe
    except FileNotFoundError:
        raise FileNotFoundError("File does not exist")

    # Verifica se o arquivo está vazio
    if not file_lines:
        raise ValueError("File is empty")

    # Loop através das linhas e conta as linhas que não são comentários ou linhas vazias
    count_lines = 0
    for line in file_lines:
        if is_not_comment_or_empty(line):
            count_lines += 1
    print(count_lines)


def check_command_line_args():
    # Verifica se há argumentos suficientes na linha de comando
    if len(sys.argv) < 2:
        raise ValueError("Too few command-line arguments")
    if len(sys.argv) > 2:
        raise ValueError("Too many command-line arguments")

    # Verifica se o arquivo de entrada é um arquivo Python válido
    if ".py" not in sys.argv[1]:
        raise ValueError("Not a Python file")


def is_not_comment_or_empty(line):
    # Verifica se a linha começa com um comentário ou é uma linha em branco
    if line.lstrip().startswith('#') or line.isspace():
        return False
    return True


if __name__ == "__main__":
    main()
