class PuntoGeografico:
    def __init__(self, latitud: float, longitud: float):
        self.latitud = latitud
        self.longitud = longitud
        self.puntos = list
    
    # Agrega las coordenadas del punto actual a la lista de puntos
    def agregarPuntos(self):
        self.puntos.append([self.latitud, self.longitud])