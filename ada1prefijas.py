class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None


class ConversorExpresiones:
    def __init__(self):
        self.precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def es_operador(self, c):
        return c in self.precedencia

    def infija_a_postfija(self, expresion):
        pila = Pila()
        salida = ""

        for c in expresion:
            if c.isalnum():  
                salida += c
            elif c == '(':
                pila.apilar(c)
            elif c == ')':
                while not pila.esta_vacia() and pila.cima() != '(':
                    salida += pila.desapilar()
                pila.desapilar() 
            elif self.es_operador(c):
                while (not pila.esta_vacia() and pila.cima() != '(' and
                       self.precedencia[pila.cima()] >= self.precedencia[c]):
                    salida += pila.desapilar()
                pila.apilar(c)

        while not pila.esta_vacia():
            salida += pila.desapilar()

        return salida

    def infija_a_prefija(self, expresion):

        expresion = expresion[::-1]
        pila = Pila()
        salida = ""

        for c in expresion:
            if c.isalnum():
                salida += c
            elif c == ')':
                pila.apilar(c)
            elif c == '(':
                while not pila.esta_vacia() and pila.cima() != ')':
                    salida += pila.desapilar()
                pila.desapilar()
            elif self.es_operador(c):
                while (not pila.esta_vacia() and pila.cima() != ')' and
                       self.precedencia[pila.cima()] > self.precedencia[c]):
                    salida += pila.desapilar()
                pila.apilar(c)

        while not pila.esta_vacia():
            salida += pila.desapilar()

        return salida[::-1]

def menu():
    conversor = ConversorExpresiones()

    while True:
        print("\n CONVERSOR DE EXPRESIONES ")
        print("1. Convertir a POSTFIJA")
        print("2. Convertir a PREFIJA")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            expresion = input("Ingrese la expresión INFJA (por ejemplo: a+b*c): ")
            resultado = conversor.infija_a_postfija(expresion)
            print(f"Expresión postfija: {resultado}")

        elif opcion == '2':
            expresion = input("Ingrese la expresión INFJA (por ejemplo: a+b*c): ")
            resultado = conversor.infija_a_prefija(expresion)
            print(f"Expresión prefija: {resultado}")

        elif opcion == '3':
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

#     4 + 4 *2 infija
