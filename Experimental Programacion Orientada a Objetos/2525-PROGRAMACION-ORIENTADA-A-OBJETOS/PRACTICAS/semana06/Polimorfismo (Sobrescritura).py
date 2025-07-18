'''
    Polimorfismo por Sobrescritura
    Sistema educativo con diferentes tipos de profesores
'''

class Profesor:
    def enseñar(self):
        print("El profesor está enseñando de forma general.")

class ProfesorMatematicas(Profesor):
    def enseñar(self):
        print("El profesor de Matemáticas está resolviendo ecuaciones.")

class ProfesorHistoria(Profesor):
    def enseñar(self):
        print("El profesor de Historia está explicando hechos históricos.")

# Lista de profesores con diferentes implementaciones del mismo método
profesores = [ProfesorMatematicas(), ProfesorHistoria()]

for profe in profesores:
    profe.enseñar()  # Cada objeto llama su versión específica del método
