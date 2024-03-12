import sys
from pathlib import Path
import unittest
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.triangulo import evaluar

class TestTriangulo(unittest.TestCase):
    def test_no_es_un_triangulo_valido(self):
        valor_esperado = "No es un triángulo válido"
        valor_actual = evaluar(3.9, 6.0, 1.2)
        self.assertEqual(valor_esperado, valor_actual)
        

    def El_triángulo_es_equilátero(self):
        valor_esperado = "El triángulo es equilátero"
        valor_actual = evaluar(1.2, 1.2, 1.2)
        self.assertEqual(valor_esperado, valor_actual)
        

    def El_triángulo_es_escaleno(self):
        valor_esperado = "El triángulo es escaleno"
        valor_actual = evaluar(3.9, 5.0, 4.2)
        self.assertEqual(valor_esperado, valor_actual)
        
    def El_triángulo_es_escaleno(self):
        valor_esperado = "El triángulo es isóceles"
        valor_actual = evaluar(4.2, 5.6, 4.2)
        self.assertEqual(valor_esperado, valor_actual)
    
    

if __name__ == '__main__':
    unittest.main()
