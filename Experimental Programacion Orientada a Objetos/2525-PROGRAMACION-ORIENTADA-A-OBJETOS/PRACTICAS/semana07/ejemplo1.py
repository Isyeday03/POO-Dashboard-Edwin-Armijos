"""
Ejemplo: Uso de Constructores y Destructores en POO con Python

Descripción:
Este programa simula la gestión de una conexión a una base de datos, utilizando los conceptos
de **constructores** y **destructores** en Programación Orientada a Objetos (POO) en Python.
"""

class ConexionBaseDatos:
    def __init__(self, nombre_bd):
        # Constructor: se llama al crear el objeto
        self.nombre_bd = nombre_bd
        print(f"Conectando a la base de datos '{self.nombre_bd}'...")

    def ejecutar_consulta(self, consulta):
        print(f"Ejecutando consulta en '{self.nombre_bd}': {consulta}")

    def __del__(self):
        # Destructor: se llama automáticamente cuando el objeto se elimina
        print(f"Cerrando conexión con la base de datos '{self.nombre_bd}'...")
        print("Chao")

# ------------------------
# Simulación del programa
# ------------------------

print("Iniciando sistema...")
conexion = ConexionBaseDatos("base_estudiantes_poo_uea")
conexion.ejecutar_consulta("SELECT * FROM estudiantes")

# El destructor se llama automáticamente cuando el objeto sale del alcance o el programa termina.
# También puedes forzar su eliminación con `del conexion`
