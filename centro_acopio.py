from turno import Turno
class CentroAcopio:
    # Patrón Singleton: nos aseguramos que solo haya una instancia de la clase en todo el sistema.
    __instance = None

    def __init__(self, nombre, turno):
        if CentroAcopio.__instance is not None:
            raise Exception("Ya existe una instancia de CentroAcopio. Utilice getInstance() para obtenerla.")
        
        self.nombre = nombre
        self.turno = turno
        self.vidrio_recolectado = 0
        self.papel_recolectado = 0
        self.plastico_recolectado = 0
        self.metal_recolectado = 0
        self.organico_recolectado = 0

        self.observadores = []

    @staticmethod
    def getInstance(nombre):
        if CentroAcopio.__instance is None:
            CentroAcopio.__instance = CentroAcopio(nombre)
        return CentroAcopio.__instance
        
    def clasificarCarga(self):
        carga = Turno.cargaTotal
        self.cantVidrio = carga * 0.2  # Suponiendo que el 20% de la carga total es vidrio
        self.cantPapel = carga * 0.3  # Suponiendo que el 30% de la carga total es papel
        self.cantPlastico = carga * 0.4  # Suponiendo que el 40% de la carga total es plástico
        self.cantMetal = carga * 0.1  # Suponiendo que el 10% de la carga total es metal
        self.cantOrganico = carga * 0.2  # Suponiendo que el 20% de la carga total es material orgánico

        # Notificar a los observadores
        for observador in self.observadores:
            observador.actualizar(self.nombre, self.cantVidrio, self.cantPapel, self.cantPlastico, self.cantMetal, self.cantOrganico)

        return self.cantVidrio, self.cantPapel, self.cantPlastico, self.cantMetal, self.cantOrganico
        
    def toneladasVidrio(self):
        return self.cantVidrio
    
    def toneladasPapel(self):
        return self.cantPapel
    
    def toneladasVidrio(self):
        return self.cantPlastico
    
    def toneladasVidrio(self):
        return self.cantMetal
    
    def toneladasVidrio(self):
        return self.cantOrganico
    
    def agregarObservador(self, observador):
        self.observadores.append(observador)
    
    def enviarActualizacionCamion(self, camion, cantVidrio, cantPapel, cantPlastico, cantMetal, cantOrganico):
        camion.notificarObservador(self.nombre, cantVidrio, cantPapel, cantPlastico, cantMetal, cantOrganico)