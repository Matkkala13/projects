"""
Tu función sum_numbers va a recibir el nodo raiz de un árbol binario con solo valores entre el 0 y 9.

Debes retornar la suma total de todos los números formados por los caminos entre la raíz y los nodos que son hojas.

Por ejemplo:

# Input
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo1.izquierda = nodo2
nodo1.derecha = nodo3

sum_numbers(nodo1)

# Output
25
"""

class Nodo:
   def __init__(self, x):
      self.valor = x
      self.izquierda = None
      self.derecha = None

def sum_numbers(raiz):
# Tu código aquí 👇
   def sum_num(raiz, acu=""):
      if raiz.izquierda == None and raiz.derecha == None:  # noqa: E711
         return acu + str(raiz.valor)

      acui = sum_num(raiz.izquierda, acu + str(raiz.valor))
      acud = sum_num(raiz.derecha, acu + str(raiz.valor))

      raiz.valor = int(acui) + int(acud)
      
      return raiz.valor
   
   raiz.valor = sum_num(raiz)
   return raiz.valor

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)
nodo7 = Nodo(7)

nodo1.izquierda = nodo2
nodo1.derecha = nodo3
nodo2.izquierda = nodo4
nodo2.derecha = nodo5

nodo3.izquierda = nodo6
nodo3.derecha = nodo7

response = sum_numbers(nodo1)
print(response)