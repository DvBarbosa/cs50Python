from datetime import date # permite trabalhar com datas
import sys # fornece informações sobre as variáveis usadas ​​pelo interpretador Python
import re # fornece funções para trabalhar com expressões regulares
import inflect  # converte números em palavras (por exemplo, "cinco" em vez de "5")

p = inflect.engine()

# Solicita a data de nascimento do usuário
def main():
    birthday = input("Date of Birth: ") # Verifica se a data de nascimento é válida usando a função check_birthday
    try:
        year, month, day = check_birthday(birthday)
    # Caso a data seja inválida, a mensagem "Invalid date" é exibida e o programa é encerrado
    except:
        sys.exit("Invalid date")
    birthDate = date(int(year), int(month), int(day)) # Criando um objeto data com a data de nascimento
    todayDate = date.today() # Criando um objeto data com a data atual
    diff = todayDate - birthDate # Calculando a diferença entre a data de nascimento e a data atual em minutos
    total_minutes = diff.days * 24 * 60
    output = p.number_to_words(total_minutes, andword='') # Convertendo o número de minutos em palavras usando o Inflect Engine
    print(output.capitalize() + " minutes") # Exibindo a quantidade de minutos em palavras na tela


def check_birthday(birthday):
    # Verificando se a data de nascimento está no formato yyyy-mm-dd usando uma expressão regular
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birthday):
        year, month, day = birthday.split("-") # Se a data de nascimento estiver no formato correto, divide-se em ano, mês e dia
        return year, month, day # Retorna o ano, mês e dia


if __name__ == "__main__":
    main()