class Pila:
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def apilar(self, disco):
        self.elementos.append(disco)

    def desapilar(self):
        if len(self.elementos) > 0:
            return self.elementos.pop()
        else:
            return None  

    def mostrar(self):
        return f"{self.nombre}: {self.elementos}"


def mover_torres(n, origen, auxiliar, destino):
    if n == 1:
        disco = origen.desapilar()
        if disco is not None:
            destino.apilar(disco)
            print(f"Mover disco {disco} de {origen.nombre} a {destino.nombre}")
    else:
        mover_torres(n - 1, origen, destino, auxiliar) 
        mover_torres(1, origen, auxiliar, destino)       
        mover_torres(n - 1, auxiliar, origen, destino)   
origen = Pila("A")
auxiliar = Pila("B")
destino = Pila("C")

for disco in [5, 4, 3, 2, 1]:
    origen.apilar(disco)

print("Estado inicial:")
print(origen.mostrar(), auxiliar.mostrar(), destino.mostrar(), "\n")

mover_torres(5, origen, auxiliar, destino)

print("\nEstado final:")
print(origen.mostrar(), auxiliar.mostrar(), destino.mostrar())
