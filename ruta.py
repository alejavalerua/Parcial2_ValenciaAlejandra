class Ruta:
    def __init__(self, nombreRuta, puntos):
        self.nombreRuta = nombreRuta
        self.puntos = puntos
        self.comandos = []

    # Agrega un punto geográfico a la ruta
    def agregarPunto(self, punto):
        self.puntos.append(punto)

    # Elimina un punto geográfico de la ruta
    def eliminarPunto(self, punto):
        self.puntos.remove(punto)

    # Agrega un comando a la ruta.
    def agregarComando(self, comando):
        self.comandos.append(comando)

    # Deshace todos los comandos almacenados en la ruta en orden inverso
    def deshacerComandos(self):
        for comando in reversed(self.comandos):
            comando.deshacer()

class Comando:
    # Ejecuta todos los comandos almacenados en la ruta
    def ejecutarComandos(self):
        for comando in self.comandos:
            comando.ejecutar()

class ComandoAgregarPunto:
    def __init__(self, ruta, punto):
        self.ruta = ruta
        self.punto = punto

    # Ejecuta el comando para agregar el punto a la ruta
    def ejecutar(self):
        self.ruta.agregar_punto(self.punto)

    # Deshace el comando, eliminando el punto de la ruta
    def deshacer(self):
        self.ruta.eliminar_punto(self.punto)

class ComandoEliminarPunto:
    def __init__(self, ruta, punto):
        self.ruta = ruta
        self.punto = punto

    # Ejecuta el comando para eliminar el punto de la ruta
    def ejecutar(self):
        self.ruta.eliminar_punto(self.punto)

    # Deshace el comando, agregando nuevamente el punto a la ruta
    def deshacer(self):
        self.ruta.agregar_punto(self.punto)
