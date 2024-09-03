import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.set_de_tenis import evaluar

class TestSetDeTenis(unittest.TestCase):
    def test_aun_no_termina_1(self):
        valor_esperado = "Aún no termina"
        valor_actual = evaluar(4, 5)
        self.assertEqual(valor_esperado, valor_actual)

    def test_aun_no_termina_2(self):
        valor_esperado = "Aún no termina"
        valor_actual = evaluar(5, 6)
        self.assertEqual(valor_esperado, valor_actual)

    def test_aun_no_termina_3(self):
        valor_esperado = "Aún no termina"
        valor_actual = evaluar(6, 6)
        self.assertEqual(valor_esperado, valor_actual)

    def test_gano_A_1(self):
        valor_esperado = "Ganó A"
        valor_actual = evaluar(6, 4)
        self.assertEqual(valor_esperado, valor_actual)

    def test_gano_A_2(self):
        valor_esperado = "Ganó A"
        valor_actual = evaluar(6, 0)
        self.assertEqual(valor_esperado, valor_actual)

    def test_gano_A_3(self):
        valor_esperado = "Ganó A"
        valor_actual = evaluar(7, 6)
        self.assertEqual(valor_esperado, valor_actual)

    def test_gano_B_1(self):
        valor_esperado = "Ganó B"
        valor_actual = evaluar(5, 7)
        self.assertEqual(valor_esperado, valor_actual)

    def test_gano_B_2(self):
        valor_esperado = "Ganó B"
        valor_actual = evaluar(0, 6)
        self.assertEqual(valor_esperado, valor_actual)

    def test_gano_B_3(self):
        valor_esperado = "Ganó B"
        valor_actual = evaluar(6, 7)
        self.assertEqual(valor_esperado, valor_actual)

    def test_invalido_1(self):
        valor_esperado = "Inválido"
        valor_actual = evaluar(3, 7)
        self.assertEqual(valor_esperado, valor_actual)

    def test_invalido_2(self):
        valor_esperado = "Inválido"
        valor_actual = evaluar(7, 0)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_invalido_3(self):
        valor_esperado = "Inválido"
        valor_actual = evaluar(0, 7)
        self.assertEqual(valor_esperado, valor_actual)

    def test_invalido_4(self):
        valor_esperado = "Inválido"
        valor_actual = evaluar(8, 6)
        self.assertEqual(valor_esperado, valor_actual)



if __name__ == '__main__':
    unittest.main()
