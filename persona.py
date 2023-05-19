class Persona:
    def __init__(self, nombre, id, turno, estrategia):
        self.nombre = nombre
        self.id = id
        self.turno = turno
        self.estrategia = estrategia

    def set_estrategia(self, estrategia):
        self.estrategia = estrategia

    def ejecutar_accion(self):
        self.estrategia.accion()