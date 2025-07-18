"""
Tarea: Aplicación de Conceptos de POO en Python

Este programa simula un sistema de gestión de animales en un zoológico.
Se aplican los conceptos de:
- Definición de clase y objeto
- Herencia
- Encapsulación (uso de atributos privados)
- Polimorfismo (sobrescritura de métodos)

"""

# Clase base
class Animal:
    def __init__(self, nombre: str, edad: int, especie: str):
        self.__nombre = nombre        # Encapsulación: atributo privado
        self.__edad = edad            # Encapsulación: atributo privado
        self.especie = especie

    # Métodos para acceder a atributos privados (getters/setters)
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad: int):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("La edad no puede ser negativa.")

    # Método que será sobrescrito (polimorfismo)
    def hacer_sonido(self):
        return "Este animal hace un sonido genérico."


# Clase derivada 1
class Perro(Animal):
    def __init__(self, nombre: str, edad: int, raza: str):
        super().__init__(nombre, edad, "Perro")
        self.raza = raza

    # Polimorfismo: sobrescribimos el método hacer_sonido
    def hacer_sonido(self):
        return "Guau guau"


# Clase derivada 2
class Gato(Animal):
    def __init__(self, nombre: str, edad: int, color: str):
        super().__init__(nombre, edad, "Gato")
        self.color = color

    # Polimorfismo: sobrescribimos el método hacer_sonido
    def hacer_sonido(self):
        return "Miau miau"


# Clase derivada 3
class Loro(Animal):
    def __init__(self, nombre: str, edad: int, puede_hablar: bool):
        super().__init__(nombre, edad, "Loro")
        self.puede_hablar = puede_hablar

    def hacer_sonido(self):
        if self.puede_hablar:
            return "¡Hola! Soy un loro que habla."
        else:
            return "Squawk squawk!"

'''
# -----------------------------
# Simulación del programa
# -----------------------------

# Crear instancias de animales
perro1 = Perro("Max", 5, "Labrador")
gato1 = Gato("Luna", 3, "Blanco")
loro1 = Loro("Kiko", 2, True)

# Mostrar comportamiento polimórfico
print("\n--- Sonidos de los animales ---")
animales = [perro1, gato1, loro1]

for animal in animales:
    print(f"{animal.get_nombre()} dice:", end=" ")
    animal.hacer_sonido()

# Demostración de encapsulamiento
print("\n--- Acceso y modificación de atributos encapsulados ---")
print(f"{perro1.get_nombre()} tiene {perro1.get_edad()} años.")
perro1.set_edad(6)
print(f"Después de cumplir años, {perro1.get_nombre()} tiene {perro1.get_edad()} años.")

# Intentar asignar una edad inválida
perro1.set_edad(-1)  # Debería mostrar un mensaje de error
'''
