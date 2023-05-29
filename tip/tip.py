def main():
    dollars = dollars_to_float(input("Quanto foi a refeição? "))
    percent = percent_to_float(input("Quanto você porcentagem dar de gorjeta? "))
    tip = dollars * percent
    print(f"Deixar ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace("$", ""))


def percent_to_float(p):
    return float(p.replace("%", "")) / 100


main()

