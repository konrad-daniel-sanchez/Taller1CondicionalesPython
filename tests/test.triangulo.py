import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.triangulo import evaluar

class TestTriangulo(unittest.TestCase):
    def test_no_valido_1(self):
        valor_esperado = "No es un triángulo válido"
        valor_actual = evaluar(1.0, 2.0, 3.0)
        self.assertEqual(valor_esperado, valor_actual)

    def test_no_valido_2(self):
        valor_esperado = "No es un triángulo válido"
        valor_actual = evaluar(4.0, 10.0, 5.0)
        self.assertEqual(valor_esperado, valor_actual)

    def test_isosceles_1(self):
        valor_esperado = "El triángulo es isósceles"
        valor_actual = evaluar(5.0, 5.0, 8.0)
        self.assertEqual(valor_esperado, valor_actual)

    def test_isosceles_2(self):
        valor_esperado = "El triángulo es isósceles"
        valor_actual = evaluar(6.0, 4.0, 6.0)
        self.assertEqual(valor_esperado, valor_actual)

    def test_escaleno_1(self):
        valor_esperado = "El triángulo es escaleno"
        valor_actual = evaluar(3.0, 5.0, 4.0)
        self.assertEqual(valor_esperado, valor_actual)

    def test_escaleno_2(self):
        valor_esperado = "El triángulo es escaleno"
        valor_actual = evaluar(6.0, 7.0, 8.0)
        self.assertEqual(valor_esperado, valor_actual)

    def test_equilatero_1(self):
        valor_esperado = "El triángulo es equilátero"
        valor_actual = evaluar(4.0, 4.0, 4.0)
        self.assertEqual(valor_esperado, valor_actual)

    def test_equilatero_2(self):
        valor_esperado = "El triángulo es equilátero"
        valor_actual = evaluar(7.5, 7.5, 7.5)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
