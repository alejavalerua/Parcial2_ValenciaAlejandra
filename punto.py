class PuntoGeografico:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        self.puntos = list
    
    def agregarPuntos(self, latitud, longitud):
        self.puntos.append([latitud, longitud])