class Jar: #Método construtor, recebe uma capacidade e define um tamanho inicial de 0
    def __init__(self, capacity=12):
        if capacity < 0: #Verifica se a capacidade é menor que 0, se for, lança uma exceção
            raise ValueError('Wrong capacity of cookies')
        self._capacity = capacity
        self._size = 0

    def __str__(self): #Método que retorna uma representação em string do pote de biscoitos
        return self.size * '🍪'

    def deposit(self, n): #Método que adiciona biscoitos ao pote, recebe como parâmetro a quantidade de biscoitos a serem adicionados
        if n > self.capacity: #Verifica se a quantidade de biscoitos a serem adicionados excede a capacidade do pote, se for, lança uma exceção
            raise ValueError("Exceed capacity")
        if self.size + n > self.capacity: #Verifica se a quantidade atual de biscoitos no pote somada à quantidade de biscoitos a serem adicionados excede a capacidade do pote, se for, lança uma exceção
            raise ValueError("Exceed capacity")
        self._size += n

    def withdraw(self, n): #Método que retira biscoitos do pote, recebe como parâmetro a quantidade de biscoitos a serem retirados
        if self.size < n:  # Verifica se a quantidade de biscoitos a serem retirados é maior que a quantidade de biscoitos atualmente no pote, se for, lança uma exceção
            raise ValueError("There are less cookies than asked to remove")
        self._size -= n #Remove os biscoitos do pote

    # Método que retorna a capacidade máxima do pote
    @property
    def capacity(self):
        return self._capacity

    #Método que retorna a quantidade atual de biscoitos no pote
    @property
    def size(self):
        return self._size