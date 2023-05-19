class Camion:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa
        self.conductor = list
        self.asistentes = list
        self.estado = CamionLibre()

    def revisarEstado(self):
        self.estado.revisarEstado()

    def cambiarEstado(self):
        self.estado.cambiarEstado(self)

    def setEstado(self, estado):
        self.estado = estado

class EstadoCamion:
    def revisarEstado(self):
        pass

    def cambiarEstado(self, camion):
        pass

class CamionLibre(EstadoCamion):
    def revisarEstado(self):
        print("El camión está libre y listo para su uso.")

    def cambiarEstado(self, camion):
        camion.setEstado(CamionOcupado())


class CamionOcupado(EstadoCamion):
    def revisarEstado(self):
        print("El camión está ocupado.")

    def cambiarEstado(self, camion):
        camion.setEstado(CamionEnMantenimiento())


class CamionEnMantenimiento(EstadoCamion):
    def revisarEstado(self):
        print("El camión está en mantenimiento y no está disponible.")

    def cambiarEstado(self, camion):
        camion.setEstado(CamionLibre())

class ObservadorCamion:
    def __init__(self, camion):
        self.camion = camion

    def actualizar(self, nombreCentroAcopio, cantVidrio, cantPapel, cantPlastico, cantMetal, cantOrganico):
        # Actualizar los registros del camión con la información recibida
        pass