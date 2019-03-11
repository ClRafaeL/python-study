from Celular import Celular
from Calculadora import Calculadora
from Matriz import Matriz

#-----------------------------------------------OBJ_CELULAR----------------------------------------------

ap = Celular('iPhone', '16 GB')

print('Modelo:', ap.modelo, ap.capacidade)
print('')

#-----------------------------------------------CALCULADORA---------------------------------------------
  
s = Calculadora()

print('soma: ', s.sum(3, 4))
print('')

print('subtração: ', s.subtr(6, 6))
print('')

print('multiplicação: ', s.multip(2, 3.5))
print('')

print('divisão: ', s.divid(3, 21))
print('')

print(s.table(10))
print('')

#-----------------------------------------------MATRIZ--------------------------------------------------

matriz = Matriz()