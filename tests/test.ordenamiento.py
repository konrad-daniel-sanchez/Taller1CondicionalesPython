import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.ordenamiento import evaluar

class TestOrdenamiento(unittest.TestCase):
    def test1(self):
        valor_esperado = "1 2 3 4"
        valor_actual = evaluar(1, 2, 3, 4)
        self.assertEqual(valor_esperado, valor_actual)

    def test2(self):
        valor_esperado = "-11 3 30 1000"
        valor_actual = evaluar(3, -11, 30, 1000)
        self.assertEqual(valor_esperado, valor_actual)

    def test3(self):
        valor_esperado = "37 452 724 1200"
        valor_actual = evaluar(724, 37, 452, 1200)
        self.assertEqual(valor_esperado, valor_actual)

    def test4(self):
        valor_esperado = "-131 27 111 324"
        valor_actual = evaluar(324, 27, -131, 111)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
