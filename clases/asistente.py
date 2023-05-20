from persona import Persona
class Asistente(Persona):
    def __init__(self, nombre, id, turno):
        super().__init__(nombre, id, turno) # --> Hereda los atributos y métodos de la clase Padre: Persona