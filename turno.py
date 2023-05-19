class Turno:
    def __init__(self, turno: int, camion, conductor, asistentes, ruta, fecha, horaInicio, horaFin, cargaTotal):
        self.turno = turno
        self.camion = camion
        self.conductor = conductor
        self.asistentes = asistentes
        self.ruta = ruta
        self.fecha = fecha
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.registros = []
        self.tiempo = self.horaFin - self.horaInicio
        self.cargaTotal = cargaTotal

    def agregarRegistro(self):
        self.registros.append((self.ruta, self.tiempo, self.cargaTotal))