from numb3rs import validate

def main():
    # Chama as 2 configuraçoes de teste
    test_format()
    test_range()

def test_format():
    # Testa se o formato de endereço ipv4 está correto
    assert validate(r'cat') == False  #Não é um formato ip
    assert validate(r'127') == False  #Não é um formato ip
    assert validate(r'127.0') == False   #Não é um formato ip
    assert validate(r'127.0.1') == False   #Não é um formato ip
    assert validate(r'127.0.1.2') == True  #é um formato ip

def test_range():
    # testa se o endereço de ip junto da range valida
    assert validate(r'255.255.255.255') == True  # Valid IP address #é um formato ip
    assert validate(r'512.1.1.1') == False  # Not a valid IP address #Não é um formato ip
    assert validate(r'1.512.1.1') == False  # Not a valid IP address #Não é um formato ip
    assert validate(r'1.1.512.1') == False  # Not a valid IP address #Não é um formato ip
    assert validate(r'1.1.1.512') == False  # Not a valid IP address #Não é um formato ip

if __name__ == "__main__":
    main()
