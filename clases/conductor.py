from persona import Persona
class Conductor(Persona):
    def __init__(self, nombre, id, turno, licencia_conducir):
        super().__init__(nombre, id, turno)  # --> Hereda los atributos y métodos de la clase Padre: Persona
        self.licencia_conducir = licencia_conducir