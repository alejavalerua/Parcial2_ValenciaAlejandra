from turno import Turno
class CentroAcopio:
    
    # Patrón Singleton: nos aseguramos que solo haya una instancia de la clase en todo el sistema.
    __instance = None

    def __init__(self, nombre, turno):
        #  Exception
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

    # Obtiene la instancia única de la clase CentroAcopio
    @staticmethod
    def getInstance(nombre):
        if CentroAcopio.__instance is None:
            CentroAcopio.__instance = CentroAcopio(nombre)
        return CentroAcopio.__instance

    # Clasifica la carga total recolectada por el turno en diferentes categorías de residuos.       
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

    # Obtiene la cantidad de toneladas de vidrio recolectadas en el centro de acopio  
    def toneladasVidrio(self):
        return self.cantVidrio
    
    # Obtiene la cantidad de toneladas de papel recolectadas en el centro de acopio
    def toneladasPapel(self):
        return self.cantPapel
    
    # Obtiene la cantidad de toneladas de plástico recolectadas en el centro de acopio
    def toneladasPlastico(self):
        return self.cantPlastico
    
    # Obtiene la cantidad de toneladas de metal recolectadas en el centro de acopio
    def toneladasMetal(self):
        return self.cantMetal
    
    # Obtiene la cantidad de toneladas de residuo orgánico recolectadas en el centro de acopio
    def toneladasOrganico(self):
        return self.cantOrganico
    
    # Agrega un observador al centro de acopio
    def agregarObservador(self, observador):
        self.observadores.append(observador)
    
    # Envía una actualización al camión con la cantidad de residuos recolectados en el centro de acopio
    def enviarActualizacionCamion(self, camion, cantVidrio, cantPapel, cantPlastico, cantMetal, cantOrganico):
        camion.notificarObservador(self.nombre, cantVidrio, cantPapel, cantPlastico, cantMetal, cantOrganico)