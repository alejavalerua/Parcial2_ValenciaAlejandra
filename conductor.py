from persona import Persona
class Conductor(Persona):
    def __init__(self, nombre, id, turno, licencia_conducir):
        super().__init__(nombre, id, turno)
        self.licencia_conducir = licencia_conducir