from punto_geografico import PuntoGeografico
from conductor import Conductor
from ruta import Ruta
from asistente import Asistente
from camion import Camion
from turno import Turno
from centro_acopio import CentroAcopio


'''import unittest

def es_palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas
    cadena = cadena.replace(" ", "").lower()
    if cadena != cadena[::-1]:
        return False
    else:
        return True

class TestPalindromo(unittest.TestCase):
    def si_es_palindromo(self):
        cadena = es_palindromo("Tomato")
        self.assertEqual(cadena, True)
    
    def no_es_palindromo(self):
        cadena = es_palindromo("Alejandra")
        self.assertFalse(cadena)
    
    def test_palindromo_vacio(self):
        resultado = es_palindromo("")
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main(exit = False)'''

# Prueba de creación de objetos
camion = Camion("Modelo1", "ABC123")
conductor = Conductor("Juan", 1, "Turno1", "Licencia123")
asistente1 = Asistente("Pedro", 2, "Turno1")
asistente2 = Asistente("María", 3, "Turno1")

# Prueba de asignación de conductor y asistentes al camión
camion.agregarConductor(conductor)
camion.agregarAsistente(asistente1)
camion.agregarAsistente(asistente2)

# Prueba de cambio de estado del camión
camion.revisarEstado()  # Estado inicial: libre
camion.cambiarEstado()  # Cambiar a estado "ocupado"
camion.revisarEstado()
camion.cambiarEstado()  # Cambiar a estado "en mantenimiento"
camion.revisarEstado()
camion.cambiarEstado()  # Cambiar a estado "libre"
camion.revisarEstado()

# Prueba de notificación de observador
observador = ObservadorCamion(camion)
camion.setObservador(observador)
camion.notificarObservador("CentroAcopio1", 10, 20, 30, 40, 50)

# Prueba de creación y manipulación de una ruta
ruta = Ruta("Ruta1", [])
punto1 = PuntoGeografico(10.123, 20.456)
punto2 = PuntoGeografico(30.789, 40.987)

ruta.agregarPunto(punto1)
ruta.agregarPunto(punto2)
print(ruta.puntos)

ruta.eliminarPunto(punto1)
print(ruta.puntos)

# Prueba de ejecución de comandos en una ruta
ruta = Ruta("Ruta2", [])
comandoAgregarPunto = ComandoAgregarPunto(ruta, punto1)
comandoEliminarPunto = ComandoEliminarPunto(ruta, punto2)

ruta.agregarComando(comandoAgregarPunto)
ruta.agregarComando(comandoEliminarPunto)

ruta.ejecutarComandos()
print(ruta.puntos)

ruta.deshacerComandos()
print(ruta.puntos)

# Prueba de registro de turno y clasificación de carga en un centro de acopio
centroAcopio = CentroAcopio.getInstance("CentroAcopio1")
turno = Turno(1, camion, conductor, [asistente1, asistente2], ruta, "2023-05-19", "08:00", "12:00", 100)

turno.agregarRegistro()

cantVidrio, cantPapel, cantPlastico, cantMetal, cantOrganico = centroAcopio.clasificarCarga()
print(f"Cantidad de vidrio: {cantVidrio}")
print(f"Cantidad de papel: {cantPapel}")
print(f"Cantidad de plástico: {cantPlastico}")
print(f"Cantidad de metal: {cantMetal}")
print(f"Cantidad de orgánico: {cantOrganico}")
