from punto_geografico import PuntoGeografico
from ruta import Ruta
from ruta import ComandoAgregarPunto
from conductor import Conductor
from asistente import Asistente
from persona import EstrategiaConductor
from persona import EstrategiaAsistente
from camion import Camion
from camion import ObservadorCamion

# Prueba 1: agregar y eliminar puntos de una ruta
ruta = Ruta("Ruta 1", [])
punto1 = PuntoGeografico(10.123, -15.678)
punto2 = PuntoGeografico(20.456, -25.789)

ruta.agregarPunto(punto1)
ruta.agregarPunto(punto2)

assert len(ruta.puntos) == 2


ruta.eliminarPunto(punto1)

assert len(ruta.puntos) == 1
assert punto1 not in ruta.puntos


# Prueba 2: ejecutar comondos en una ruta
ruta = Ruta("Ruta 1", [])
punto1 = PuntoGeografico(10.123, -15.678)
punto2 = PuntoGeografico(20.456, -25.789)

comando1 = ComandoAgregarPunto(ruta, punto1)
comando2 = ComandoAgregarPunto(ruta, punto2)

ruta.agregarComando(comando1)
ruta.agregarComando(comando2)

ruta.deshacerComandos()

assert len(ruta.puntos) == 0


# Prueba 3: establecer estrategia y ejecutar acción de una persona
estrategia_conductor = EstrategiaConductor()
estrategia_asistente = EstrategiaAsistente()

conductor = Conductor("Juan", 1, "Mañana", "Licencia123")
asistente = Asistente("María", 2, "Tarde")

conductor.estrategia.set_estrategia(estrategia_conductor)
asistente.estrategia.set_estrategia(estrategia_asistente)

assert conductor.estrategia == estrategia_conductor
assert asistente.estrategia == estrategia_asistente

conductor.estrategia.ejecutarAccion()  # Salida esperada: "Conduciendo el camión"
asistente.estrategia.ejecutarAccion()  # Salida esperada: "Asistiendo en la recolección de residuos"


# Prueba 4: cambiar el estado de un camión
camion = Camion("Modelo1", "ABC123")
observador = ObservadorCamion(camion)
camion.setObservador(observador)

camion.revisarEstado()  # Salida esperada: "El camión está libre y listo para su uso."

camion.cambiarEstado()  # Cambiar de estado de libre a ocupado
camion.revisarEstado()  # Salida esperada: "El camión está ocupado."

camion.cambiarEstado()  # Cambiar de estado de ocupado a en mantenimiento
camion.revisarEstado()  # Salida esperada: "El camión está en mantenimiento y no está disponible."

camion.cambiarEstado()  # Cambiar de estado de en mantenimiento a libre
camion.revisarEstado()  # Salida esperada: "El camión está libre y listo para su uso."