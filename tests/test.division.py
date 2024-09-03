import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.division import evaluar

class TestDivision(unittest.TestCase):
    def testDivision1(self):
        valor_esperado = "La división no es exacta. \n" \
                         "Cociente: 2\n" \
                         "Residuo: 4"
        valor_actual = evaluar(14, 5)
        self.assertEqual(valor_esperado, valor_actual)

    def testDivision2(self):
        valor_esperado = "La división no es exacta. \n" \
                         "Cociente: 16\n" \
                         "Residuo: 1"
        valor_actual = evaluar(17, 4)
        self.assertEqual(valor_esperado, valor_actual)

    def testDivision3(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 234\n" \
                         "Residuo: 0"
        valor_actual = evaluar(2340, 10)
        self.assertEqual(valor_esperado, valor_actual)

    def testDivision4(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 2386\n" \
                         "Residuo: 0"
        valor_actual = evaluar(238600, 100)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
