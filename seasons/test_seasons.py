from seasons import check_birthday
#Acima importa Seasons para teste e importa a def main(): check birthday
def main():
    test_check_birthday()
#função que testa o aniversario
def test_check_birthday():
    assert check_birthday("July 3, 1998") == None #se for feita dessa forma, nao retorna nada
    assert check_birthday("1998-7-3") == None #se for feita dessa forma, nao retorna nada
    assert check_birthday("1998-07-03") == ("1998", "07", "03") #se for dessa forma, vai retornar o valor dizendo a quantidade de minutos, considerando que o dia é 01-01-2001

if __name__ == "__main__":
    main()