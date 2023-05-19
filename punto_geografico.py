class PuntoGeografico:
    def __init__(self, latitud: float, longitud: float):
        self.latitud = latitud
        self.longitud = longitud
        self.puntos = list
    
    def agregarPuntos(self):
        self.puntos.append([self.latitud, self.longitud])