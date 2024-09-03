import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.annos_bisiestos import evaluar

class TestAnnosBisiestos(unittest.TestCase):
    def test_1988(self):
        valor_esperado = "1988 es bisiesto"
        valor_actual = evaluar(1988)
        self.assertEqual(valor_esperado, valor_actual)

    def test_1990(self):
        valor_esperado = "1990 no es bisiesto"
        valor_actual = evaluar(1990)
        self.assertEqual(valor_esperado, valor_actual)

    def test_2020(self):
        valor_esperado = "2020 es bisiesto"
        valor_actual = evaluar(2020)
        self.assertEqual(valor_esperado, valor_actual)

    def test_1900(self):
        valor_esperado = "1900 no es bisiesto"
        valor_actual = evaluar(1900)
        self.assertEqual(valor_esperado, valor_actual)

    def test_2400(self):
        valor_esperado = "2400 es bisiesto"
        valor_actual = evaluar(2400)
        self.assertEqual(valor_esperado, valor_actual)
    
if __name__ == '__main__':
    unittest.main()
