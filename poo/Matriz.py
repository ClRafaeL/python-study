class Matriz():
    matriz = []

    def receive_tam_matriz(self, lado1, lado2):
            lado1 = input('informe o 1º lado da matriz: ')
            lado2 = input('informe o 2º lado da matriz: ')

    def create_matriz(self, x, y):
        self.lado1 = x
        self.lado2 = y
        self.matriz = [x, y]

    def increment_matriz(self, x):
        for i in range(0, x):
            self.matriz.append(input('digite {}º valor da matriz: '. format(i)))

    def imprimi(self, matriz):
        return print('matriz formada: ', self.matriz)