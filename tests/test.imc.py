import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.imc import evaluar

class TestIMC(unittest.TestCase):
    def testBajo1(self):
        valor_esperado = "bajo"
        valor_actual = evaluar(50, 1.8,20)
        self.assertEqual(valor_esperado, valor_actual)

    def testBajo2(self):
        valor_esperado = "bajo"
        valor_actual = evaluar(56, 1.6,44)
        self.assertEqual(valor_esperado, valor_actual)

    def testMedio1(self):
        valor_esperado = "medio"
        valor_actual = evaluar(70, 1.7, 25)
        self.assertEqual(valor_esperado, valor_actual)

    def testMedio2(self):
        valor_esperado = "medio"
        valor_actual = evaluar(55, 1.75, 45)
        self.assertEqual(valor_esperado, valor_actual)

    def testAlto1(self):
        valor_esperado = "alto"
        valor_actual = evaluar(90, 1.72, 50)
        self.assertEqual(valor_esperado, valor_actual)

    def testAlto2(self):
        valor_esperado = "alto"
        valor_actual = evaluar(100, 2.0, 45)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
