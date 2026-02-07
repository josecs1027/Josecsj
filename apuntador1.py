# Nodo básico para la pila
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Pila con nodos enlazados
class Pila:
    def __init__(self):
        self.tope = None

    def push(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def pop(self):
        if self.tope is None:
            print("Pila vacía")
            return
        valor = self.tope.valor
        self.tope = self.tope.siguiente
        print("Elemento eliminado:", valor)

    def mostrar(self):
        actual = self.tope
        if actual is None:
            print("Pila vacía")
            return
        print("Pila (tope ↓):")
        while actual:
            print(actual.valor)
            actual = actual.siguiente

# Menú interactivo con ingreso por teclado
def menu():
    p = Pila()
    while True:
        print("\n--- MENÚ PILA LIGADA ---")
        print("1. Insertar elemento (push)")
        print("2. Eliminar elemento (pop)")
        print("3. Mostrar pila")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            valor = input("Ingresa un valor para la pila: ")
            p.push(valor)
        elif opcion == "2":
            p.pop()
        elif opcion == "3":
            p.mostrar()
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
menu()
