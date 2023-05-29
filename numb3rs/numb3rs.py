import re

def main():
    # Prompt para o usuario fornecer o ipv4 de entrada, e imprimir o resultado da funcao validada
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Checka se a string d entrada coincide com o formato ipv4(4 numeros separados por dots)
    if re.search(r"^[0-9_]+\.[0-9_]+\.[0-9_]+\.[0-9_]+$", ip):
        # separa o endereço de ip em 4 pedaços
        split_ip = ip.split(".")
        # Checa se cada peça está entre 0 e 255
        for piece in split_ip:
            if int(piece) > 255:
                return False
        # se todas as 4 peças forem validas, retorne Verdadeiro
        return True
    else:
        # Se a entrada de usuario está ou nao match com o formato ipv4, retorne Falso
        return False

if __name__ == "__main__":
    main()
