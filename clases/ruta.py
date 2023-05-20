from punto_geografico import PuntoGeografico

# Clase que representa una ruta que contiene puntos geográficos y comandos asociados
class Ruta:
    def __init__(self, nombreRuta, puntos = None):
        self.nombreRuta = nombreRuta
        if puntos is None:
            self.puntos = []  # Inicializar la lista de puntos si no se proporciona
        else:
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
            self.comandos.remove(comando)

# Clase base abstracta para un comando en una ruta.
class Comando:
    # Ejecuta el comando
    def ejecutar(self):
        pass

    # Deshace el comando
    def deshacer(self):
        pass

# Clase que representa un comando para agregar un punto a una ruta
class ComandoAgregarPunto:
    def __init__(self, ruta, punto):
        self.ruta = ruta  # Ruta a la cual se agregará el punto
        self.punto = punto  # Punto a agregar

    # Ejecuta el comando para agregar el punto a la ruta
    def ejecutar(self):
        self.ruta.agregarPunto(self.punto)

    # Deshace el comando, eliminando el punto de la ruta
    def deshacer(self):
        self.ruta.eliminarPunto(self.punto)

# Clase que representa un comando para eliminar un punto de una ruta
class ComandoEliminarPunto:
    def __init__(self, ruta, punto):
        self.ruta = ruta  # Ruta de la cual se eliminará el punto
        self.punto = punto  # Punto a eliminar

    # Ejecuta el comando para eliminar el punto de la ruta
    def ejecutar(self):
        self.ruta.eliminarPunto(self.punto)

    # Deshace el comando, agregando nuevamente el punto a la ruta
    def deshacer(self):
        self.ruta.agregarPunto(self.punto)