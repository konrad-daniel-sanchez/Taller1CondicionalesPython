import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.edad import evaluar

class TestEdad(unittest.TestCase):
    def test1(self):
        valor_esperado = "Usted tiene 23 años"
        valor_actual = evaluar(31, 12, 2000)
        self.assertEqual(valor_esperado, valor_actual)

    def test2(self):
        valor_esperado = "Usted tiene 19 años"
        valor_actual = evaluar(27, 8, 2005)
        self.assertEqual(valor_esperado, valor_actual)

    def test3(self):
        valor_esperado = "Usted tiene 21 años"
        valor_actual = evaluar(31, 8, 2003)
        self.assertEqual(valor_esperado, valor_actual)

    def test4(self):
        valor_esperado = "Usted tiene 60 años"
        valor_actual = evaluar(2, 9, 1964)
        self.assertEqual(valor_esperado, valor_actual)
    
if __name__ == '__main__':
    unittest.main()
