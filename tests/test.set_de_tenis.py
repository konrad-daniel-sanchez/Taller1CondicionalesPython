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
    def test_aun_no_termina(self):
        valor_esperado = "Aún no termina"
        valor_actual = evaluar(4, 5)
        self.assertEqual(valor_esperado, valor_actual)
    
    # TODO: Agrega tus otros casos de prueba aquí
    

if __name__ == '__main__':
    unittest.main()
