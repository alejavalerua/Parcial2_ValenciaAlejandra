class Ruta:
    def __init__(self, nombreRuta, puntos):
        self.nombreRuta = nombreRuta
        self.puntos = puntos
        self.comandos = []

    def agregarPunto(self, punto):
        self.puntos.append(punto)

    def eliminarPunto(self, punto):
        self.puntos.remove(punto)

    def ejecutarComandos(self):
        for comando in self.comandos:
            comando.ejecutar()

    def agregarComando(self, comando):
        self.comandos.append(comando)

    def deshacerComandos(self):
        for comando in reversed(self.comandos):
            comando.deshacer()

class ComandoAgregarPunto:
    def __init__(self, ruta, punto):
        self.ruta = ruta
        self.punto = punto

    def ejecutar(self):
        self.ruta.agregar_punto(self.punto)

    def deshacer(self):
        self.ruta.eliminar_punto(self.punto)

class ComandoEliminarPunto:
    def __init__(self, ruta, punto):
        self.ruta = ruta
        self.punto = punto

    def ejecutar(self):
        self.ruta.eliminar_punto(self.punto)

    def deshacer(self):
        self.ruta.agregar_punto(self.punto)