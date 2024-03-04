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
    def testNo(self):
        valor_esperado = "0 1 6 7"
        valor_actual = evaluar(7, 0, 6, 1)
        self.assertEqual(valor_esperado, valor_actual)
    
    # TODO: Agrega tus otros casos de prueba aquí
    

if __name__ == '__main__':
    unittest.main()
