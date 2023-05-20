from punto_geografico import PuntoGeografico
from ruta import Ruta
from ruta import ComandoAgregarPunto
import unittest

'''class RutaTestCase(unittest.TestCase):
    def setUp(self):
        self.ruta = Ruta("Ruta 1", [])

    def test_agregar_punto(self):
        punto = PuntoGeografico(10.0, 20.0)
        self.ruta.agregarPunto(punto)
        self.assertEqual(len(self.ruta.puntos), 1)
        self.assertEqual(self.ruta.puntos[0], punto)

    def test_eliminar_punto(self):
        punto = PuntoGeografico(10.0, 20.0)
        self.ruta.agregarPunto(punto)
        self.ruta.eliminarPunto(punto)
        self.assertEqual(len(self.ruta.puntos), 0)

    def test_agregar_comando(self):
        comando = ComandoAgregarPunto(self.ruta, PuntoGeografico(10.0, 20.0))
        self.ruta.agregarComando(comando)
        self.assertEqual(len(self.ruta.comandos), 1)
        self.assertEqual(self.ruta.comandos[0], comando)

    def test_deshacer_comandos(self):
        punto = PuntoGeografico(10.0, 20.0)
        comando = ComandoAgregarPunto(self.ruta, punto)
        self.ruta.agregarComando(comando)
        self.ruta.deshacerComandos(comando)
        self.assertEqual(len(self.ruta.puntos), 0)

if __name__ == '__main__':
    unittest.main()'''

# Prueba de agregar y eliminar puntos de una ruta
ruta = Ruta("Ruta 1", [])
punto1 = PuntoGeografico(10.123, -15.678)
punto2 = PuntoGeografico(20.456, -25.789)

ruta.agregarPunto(punto1)
ruta.agregarPunto(punto2)

assert len(ruta.puntos) == 2


ruta.eliminarPunto(punto1)

assert len(ruta.puntos) == 1
assert punto1 not in ruta.puntos