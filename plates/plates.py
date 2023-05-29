def is_valid(s):
    # Requisito 1: Todas as placas devem começar com pelo menos 2 letras.
    if not s[:2].isalpha():
        return False

    # Requisito 2: As placas devem conter no máximo, 6 caracteres, e um mínimo de 2 caracteres.
    if not 2 <= len(s) <= 6:
        return False

    # Requisito 3: Números não podem ser usados no meio da placa, eles devem ser usados no fim.
    if not s[-1].isnumeric():
        if not s[2:-1].isalpha():
            return False
    else:
        if not s[2:-1].isdigit():
            return False

    # Requisito 4: Espaços, acentos ou pontuações não podem ser aceitas.
    if not s.isalnum():
        return False

    return True


def main():
    plate = input("Plate:")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


main()
