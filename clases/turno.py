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

    # Agrega un registro del turno a la lista de registros
    def agregarRegistro(self):
        self.registros.append((self.ruta, self.tiempo, self.cargaTotal))
    
    # Calcula la cantidad total de vidrio recolectado durante el día especificado
    def vidrioRecolectadoDia(self, turnos, fecha):
        vidrioTotal = 0
        for turno in turnos:
            if turno.fecha == fecha:
                vidrioTotal += turno.toneladasVidrio()
        return f"En el día se recolectaron {vidrioTotal} kg de vidrio."
    
    # Calcula la cantidad total de papel recolectado durante el día especificado
    def papelRecolectadoDia(self, turnos, fecha):
        papelTotal = 0
        for turno in turnos:
            if turno.fecha == fecha:
                papelTotal += turno.toneladasPapel()
        return f"En el día se recolectaron {papelTotal} kg de papel."
    
    # Calcula la cantidad total de plástico recolectado durante el día especificado
    def plasticoRecolectadoDia(self, turnos, fecha):
        plasticoTotal = 0
        for turno in turnos:
            if turno.fecha == fecha:
                plasticoTotal += turno.toneladasPlastico()
        return f"En el día se recolectaron {plasticoTotal} kg de plástico."
    
    # Calcula la cantidad total de metal recolectado durante el día especificado
    def metalRecolectadoDia(self, turnos, fecha):
        metalTotal = 0
        for turno in turnos:
            if turno.fecha == fecha:
                metalTotal += turno.toneladasMetal()
        return f"En el día se recolectaron {metalTotal} kg de metal."
    
    # Calcula la cantidad total de material orgánico recolectado durante el día especificado
    def organicoRecolectadoDia(self, turnos, fecha):
        organicoTotal = 0
        for turno in turnos:
            if turno.fecha == fecha:
                organicoTotal += turno.toneladasOrganico()
        return f"En el día se recolectaron {organicoTotal} kg de material orgánico."