# Programa diseñado para la empresa de manejo de residuos “TrashCity”

from datetime import datetime
from punto_geografico import PuntoGeografico
from conductor import Conductor
from ruta import Ruta
from asistente import Asistente
from camion import Camion
from turno import Turno

# Creamos objetos PuntoGeografico para los puntos de la ruta
punto1 = PuntoGeografico(6.2498, -75.5636)
punto2 = PuntoGeografico(6.2620, -75.5790)
punto3 = PuntoGeografico(6.2462, -75.5692)

# Creamos un objeto Ruta
ruta1 = Ruta("Ruta 1", [punto1, punto2, punto3])

# Creamos objetos Conductor y Asistente
conductor1 = Conductor("Juan", "12345", "Mañana", "B1")
asistente1 = Asistente("Pedro", "67890", "Mañana")
asistente2 = Asistente("María", "24680", "Mañana")

# Creamos un objeto Camion
camion1 = Camion("Ford", "ABC123")

# Agregamos un conductor y sus asistentes al objeto camion1
camion1.conductor = conductor1
camion1.asistentes = [asistente1, asistente2]

# Creamos un objeto Turno
turno1 = Turno(1, camion1, conductor1, [asistente1, asistente2], ruta1, datetime.now(), datetime(2023, 3, 31, 8), datetime(2023, 3, 31, 12))

# Agregamos registros al objeto Turno1
fecha = datetime.now().date()
horaInicio = 630
horaFin = 1400

turno1 = Turno(1, camion1, conductor1, [asistente1, asistente2], ruta1, fecha, horaInicio, horaFin)
turno1.agregarRegistro(punto1, 630, 30)
turno1.agregarRegistro(punto2, 700, 55)
turno1.agregarRegistro(punto3, 745, 75)

turno2 = Turno(2, camion1, conductor1, [asistente1, asistente2], ruta1, fecha, horaInicio, horaFin)
turno2.agregarRegistro(punto1, 800, 120)
turno2.agregarRegistro(punto2, 830, 25)
turno2.agregarRegistro(punto3, 1000, 250)

turno3 = Turno(3, camion1, conductor1, [asistente1, asistente2], ruta1, fecha, horaInicio, horaFin)
turno3.agregarRegistro(punto1, 1100, 300)
turno3.agregarRegistro(punto2, 1200, 450)
turno3.agregarRegistro(punto3, 1330, 650)

# Calcular la cantidad total de vidrio recolectado en el día
turnos = [turno1, turno2, turno3]
vidrio_total = turno1.vidrioRecolectadoDia(turnos, fecha)
print("Cantidad total de vidrio recolectado en el día: ", vidrio_total, "kg")

# Ejemplo de uso
# ruta = Ruta("Ruta1", ["Punto A", "Punto B", "Punto C"])
# print(ruta.puntos)  # Salida: ['Punto A', 'Punto B', 'Punto C']

# comando_agregar = ComandoAgregarPunto(ruta, "Punto D")
# ruta.agregar_comando(comando_agregar)
# ruta.ejecutar_comandos()

# print(ruta.puntos)  # Salida: ['Punto A', 'Punto B', 'Punto C', 'Punto D']

# comando_eliminar = ComandoEliminarPunto(ruta, "Punto B")
# ruta.agregar_comando(comando_eliminar)
#  ruta.ejecutar_comandos()

# print(ruta.puntos)  # Salida: ['Punto A', 'Punto C', 'Punto D']

# ruta.deshacer_comandos()

# print(ruta.puntos)  # Salida: ['Punto A', 'Punto B', 'Punto C', 'Punto D']