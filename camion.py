class Camion:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa
        self.conductor = list
        self.asistentes = list
        self.estado = CamionLibre()
        self.observador = None

    # Agrega un conductor al camión.
    def agregarConductor(self, conductor):
        self.conductor.append(conductor)

    # Agrega un asistente al camión
    def agregarAsistente(self, asistente):
        self.asistentes.append(asistente)

    # Revisa el estado actual del camión
    def revisarEstado(self):
        self.estado.revisarEstado()

    # Cambia el estado del camión
    def cambiarEstado(self):
        self.estado.cambiarEstado(self)

    # Establece el estado del camión
    def setEstado(self, estado):
        self.estado = estado

    # Establece un observador para el camión
    def setObservador(self, observador):
        self.observador = observador

    # Notifica al observador del camión con la información recibida
    def notificarObservador(self, nombreCentroAcopio, cantVidrio, cantPapel, cantPlastico, cantMetal, cantOrganico):
        if self.observador:
            self.observador.actualizar(nombreCentroAcopio, cantVidrio, cantPapel, cantPlastico, cantMetal, cantOrganico)

class EstadoCamion:
    # Revisa el estado del camión
    def revisarEstado(self):
        pass

    # Cambia el estado del camión
    def cambiarEstado(self, camion):
        pass

class CamionLibre(EstadoCamion):
    # Revisa el estado del camión libre
    def revisarEstado(self):
        print("El camión está libre y listo para su uso.")

    # Cambia el estado del camión libre al estado de camión ocupado
    def cambiarEstado(self, camion):
        camion.setEstado(CamionOcupado())

class CamionOcupado(EstadoCamion):
    # Revisa el estado del camión ocupado
    def revisarEstado(self):
        print("El camión está ocupado.")

    # Cambia el estado del camión ocupado al estado de camión en mantenimiento
    def cambiarEstado(self, camion):
        camion.setEstado(CamionEnMantenimiento())

class CamionEnMantenimiento(EstadoCamion):
    # Revisa el estado del camión en mantenimiento
    def revisarEstado(self):
        print("El camión está en mantenimiento y no está disponible.")

    # Cambia el estado del camión en mantenimiento al estado de camión libre
    def cambiarEstado(self, camion):
        camion.setEstado(CamionLibre())

class ObservadorCamion:
    def __init__(self, camion):
        self.camion = camion

    # Actualiza el observador con la información recibida
    def actualizar(self, nombreCentroAcopio, cantVidrio, cantPapel, cantPlastico, cantMetal, cantOrganico):
        # Actualizar los registros del camión con la información recibida
        print(f"El camión ha llegado al centro de acopio {nombreCentroAcopio}.")
        print(f"Se ha recolectado la siguiente cantidad de materiales:")
        print(f"Vidrio: {cantVidrio} kg")
        print(f"Papel: {cantPapel} kg")
        print(f"Plástico: {cantPlastico} kg")
        print(f"Metal: {cantMetal} kg")
        print(f"Orgánico: {cantOrganico} kg")