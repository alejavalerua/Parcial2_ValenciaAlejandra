import unittest
from punto_geografico import PuntoGeografico
from ruta import Ruta
from ruta import ComandoAgregarPunto
from ruta import ComandoEliminarPunto

class RutaTestCase(unittest.TestCase):
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
        punto1 = PuntoGeografico(10.0, 20.0)
        punto2 = PuntoGeografico(30.0, 40.0)
        comando1 = ComandoAgregarPunto(self.ruta, punto1)
        comando2 = ComandoAgregarPunto(self.ruta, punto2)
        self.ruta.agregarComando(comando1)
        self.ruta.agregarComando(comando2)
        self.assertEqual(len(self.ruta.puntos), 2)
        self.ruta.deshacerComandos()
        self.assertEqual(len(self.ruta.puntos), 2)

    def test_deshacer_comandos_con_eliminar_punto(self):
        punto = PuntoGeografico(10.0, 20.0)
        comando1 = ComandoAgregarPunto(self.ruta, punto)
        comando2 = ComandoEliminarPunto(self.ruta, punto)
        self.ruta.agregarComando(comando1)
        self.ruta.agregarComando(comando2)
        self.assertEqual(len(self.ruta.puntos), 0)
        self.ruta.deshacerComandos()
        self.assertEqual(len(self.ruta.puntos), 1)
        self.assertEqual(self.ruta.puntos[0], punto)

    def test_nombre_ruta(self):
        self.assertEqual(self.ruta.nombreRuta, "Ruta 1")

    def test_deshacer_comandos_sin_comandos(self):
        self.ruta.deshacerComandos() # No debería lanzar ninguna excepción

if __name__ == '__main__':
    unittest.main()
