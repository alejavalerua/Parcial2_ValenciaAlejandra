class Persona:
    def __init__(self, nombre, id, turno, estrategia):
        self.nombre = nombre
        self.id = id
        self.turno = turno
        self.estrategia = estrategia

class Estrategia:
    ''' Establece la estrategia de acción de la persona -->
        estrategia (EstrategiaConductor o EstrategiaAsistente): Estrategia de acción de la persona.'''
    def set_estrategia(self, estrategia):
        Persona.estrategia = estrategia

    # Ejecuta la acción de la persona según su estrategia
    def ejecutar_accion(self):
        Persona.estrategia.accion()

class EstrategiaConductor:
    # Ejecuta la estrategia de acción del conductor
    def accion(self):
        print("Conduciendo el camión")

class EstrategiaAsistente:
    # Ejecuta la estrategia de acción del asistente
    def accion(self):
        print("Asistiendo en la recolección de residuos")