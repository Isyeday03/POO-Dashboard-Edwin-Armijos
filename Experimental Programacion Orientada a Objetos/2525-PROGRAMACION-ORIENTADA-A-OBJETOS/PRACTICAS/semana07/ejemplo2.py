''''
Simular el inicio de sesión y actividades de usuarios en una plataforma.
'''

# Clase que representa a un usuario del sistema
class Usuario:
    def __init__(self, nombre: str, correo: str):
        # Constructor: se ejecuta al crear una instancia de Usuario
        self.nombre = nombre
        self.correo = correo
        print(f"Usuario '{self.nombre}' creado con el correo: {self.correo}")

    def saludar(self):
        # Método que imprime un saludo personalizado
        print(f"Hola, soy {self.nombre}. ¡Bienvenido al sistema!")

    def __del__(self):
        # Destructor: se ejecuta automáticamente cuando el objeto es destruido
        # Aquí se usa solo para registrar un cierre de sesión simulado
        print(f"El usuario '{self.nombre}' ha cerrado sesión.")


# Clase que representa una plataforma o sistema donde se registran los usuarios
class Plataforma:
    def __init__(self, nombre):
        # Constructor: inicializa la plataforma con un nombre y una lista vacía de usuarios
        self.nombre = nombre
        self.usuarios = []
        print(f"️Plataforma '{self.nombre}' iniciada.")

    def registrar_usuario(self, usuario: Usuario):
        # Método para registrar un usuario en la plataforma
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' registrado en la plataforma '{self.nombre}'.")

    def mostrar_usuarios(self):
        # Método para mostrar todos los usuarios registrados
        print(f"👥 Usuarios en la plataforma '{self.nombre}':")
        for u in self.usuarios:
            print(f" - {u.nombre} ({u.correo})")


# -----------------------------
# Simulación del sistema
# -----------------------------

# Crear una plataforma
plataforma = Plataforma("Curso de Programación Orientada a Objetos.")

# Crear dos usuarios
usuario1 = Usuario("Carlos Pérez", "carlos@uea.edu.ec")
usuario2 = Usuario("Ana López", "ana@uea.edu.ec")
usuario3 = Usuario("Santiago Nogales", "santiago@uea.edu.ec")

# Registrar los usuarios en la plataforma
plataforma.registrar_usuario(usuario1)
plataforma.registrar_usuario(usuario2)
plataforma.registrar_usuario(usuario3)

# Realizar actividades: saludo personalizado
print("\n--- Actividades ---")
usuario1.saludar()
usuario2.saludar()
usuario3.saludar()

# Mostrar todos los usuarios registrados
print("\n--- Lista de usuarios ---")
plataforma.mostrar_usuarios()

# Cuando el programa termina, los destructores (__del__) se ejecutan automáticamente,
# simulando el cierre de sesión de cada usuario.
