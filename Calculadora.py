class Calculadora():
    def sum(self, x, y):
        self.num1 = x
        self.num2 = y
        return x + y

    def subtr(self, a, b):
        return a - b

    def multip(self, x, y):
        return x * y

    def divid(self, x, y):
        return x / y
    
    def table(self, x):        
        for y in range(0, 11):
            print(' {} x {} = {}' .format(x, y, x*y))