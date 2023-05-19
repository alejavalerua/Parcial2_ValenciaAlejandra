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
    
    def vidrioRecolectadoDia(self, turnos, fecha):
        vidrioTotal = 0
        for turno in turnos:
            if turno.fecha == fecha:
                vidrioTotal += turno.toneladasVidrio()
        return vidrioTotal
    
    def papelRecolectadoDia(self, turnos, fecha):
        papelTotal = 0
        for turno in turnos:
            if turno.fecha == fecha:
                papelTotal += turno.toneladasPapel()
        return papelTotal
    
    def plasticoRecolectadoDia(self, turnos, fecha):
        plasticoTotal = 0
        for turno in turnos:
            if turno.fecha == fecha:
                plasticoTotal += turno.toneladasPlastico()
        return plasticoTotal
    
    def metalRecolectadoDia(self, turnos, fecha):
        metalTotal = 0
        for turno in turnos:
            if turno.fecha == fecha:
                metalTotal += turno.toneladasMetal()
        return metalTotal
    
    def organicoRecolectadoDia(self, turnos, fecha):
        organicoTotal = 0
        for turno in turnos:
            if turno.fecha == fecha:
                organicoTotal += turno.toneladasOrganico()
        return organicoTotal