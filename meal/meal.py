def main():
    time_str = input("Enter a time in 24-hour format (hh:mm): ")
    try:
        hours = convert(time_str)
    except ValueError:
        print("Invalid time format")
        return
    #se 7 for igual ou maior a 11, diga "hora do café"
    if 7 <= hours < 11:
        print("breakfast time")
    elif 11 <= hours < 14: #enquanto 11 for igual ou maior que 14, entao diga "hora do almoço"
        print("lunch time")
    elif 17 <= hours < 20: #enquanto 17 for igual ou maior que 20, então diga "hora do jantar"
        print("dinner time")

#eu acredito que nao seja nada muito complexo. aqui fica uma def que serve para converter o tempo, em almoço, café ou jantar
#funciona da seguinte forma. Horas e Minutos é igual a tempo.split (":")
#retorna Float(Horas) e soma com Float(minutos) e divide por 60
def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
