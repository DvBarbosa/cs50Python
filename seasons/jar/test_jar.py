from jar import Jar

def main(): #A função main é a função principal do programa e é responsável por chamar todas as funções de teste.
    test_init()
    test_str()
    test_deposit()

def test_init(): #A função test_init testa se a inicialização da classe Jar está funcionando corretamente.
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(3)
    assert jar2.capacity == 3

def test_str(): #A função test_str testa se o método __str__ da classe Jar está funcionando corretamente.
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit(): #Afunção test_deposit testa se o método deposit da classe Jar está funcionando corretamente. Nela, é criada uma instância da classe Jar e é verificado se o atributo size dessa instância está correto após fazer alguns depósitos.
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3

def test_withdraw(): #A função test_withdraw testa se o método withdraw da classe Jar está funcionando corretamente. Nela, é criada uma instância da classe Jar, é feito um depósito e em seguida é verificado se o atributo size dessa instância está correto após fazer uma retirada de cookies.
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1

#As funções main, test_init, test_str, test_deposit e test_withdraw são responsáveis por testar a classe Jar.]

