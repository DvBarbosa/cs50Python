import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Verifica se a string de entrada está no formato correto
    isCorrectFormat = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if isCorrectFormat:
        # Extrai as informações de cada hora da string de entrada
        pieces = isCorrectFormat.groups()
        # Verifica se as horas estão no formato correto (de 1 a 12)
        if int(pieces[1]) > 12 or int(pieces[5]) > 12:
            # Levanta um erro caso as horas estejam incorretas
            raise ValueError
        # Cria a primeira hora no formato correto de 24 horas
        first_time = new_format(pieces[1], pieces[2], pieces[3])
        # Cria a segunda hora no formato correto de 24 horas
        second_time = new_format(pieces[5], pieces[6], pieces[7])
        # Retorna as duas horas no formato correto
        return first_time + " to " + second_time
    else:
        # Levanta um erro caso a entrada esteja no formato incorreto
        raise ValueError

def new_format(hour, minutes, am_pm):
    # Converte a hora para o formato correto de 24 horas
    if am_pm == 'PM':
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    # Formata a hora de acordo com o número de minutos
    if minutes == None:
        new_time = f"{new_hour:02}" + ":00"
    else:
        new_time = f"{new_hour:02}" + ":" + minutes
    # Retorna a hora no formato correto
    return new_time

if __name__ == "__main__":
    main()
