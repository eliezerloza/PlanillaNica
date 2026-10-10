import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

os.environ.setdefault("PLANILLA_SECRET_KEY", "clave-pruebas-temporal")

from app import numero_positivo
from database import calcular_ir_nicaragua


class TestPlanilla(unittest.TestCase):

    def test_numero_positivo_valido(self):
        self.assertEqual(numero_positivo("1500", "Salario"), 1500.0)

    def test_numero_positivo_rechaza_texto(self):
        with self.assertRaises(ValueError):
            numero_positivo("abc", "Salario")

    def test_numero_positivo_rechaza_negativos(self):
        with self.assertRaises(ValueError):
            numero_positivo("-100", "Salario")

    def test_numero_positivo_rechaza_cero(self):
        with self.assertRaises(ValueError):
            numero_positivo("0", "Salario", permite_cero=False)

    def test_ir_sin_impuesto(self):
        self.assertEqual(calcular_ir_nicaragua(8000, 560), 0.0)

    def test_ir_con_impuesto(self):
        self.assertGreater(calcular_ir_nicaragua(15000, 1050), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
