from persona import Persona
class Asistente(Persona):
    def __init__(self, nombre, id, turno):
        super().__init__(nombre, id, turno)

class EstrategiaAsistente:
    def accion(self):
        print("Asistiendo en la recolección de residuos")