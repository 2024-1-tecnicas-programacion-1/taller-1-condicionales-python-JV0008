import sys
from pathlib import Path
import unittest
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.edad import evaluar

class TestEdad(unittest.TestCase):
    def test2000Enero1(self):
        valor_esperado = 'Usted tiene 24 años'
        valor_actual = evaluar(1, 1, 2000)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test2020Marzo9(self):
        valor_esperado = 'Usted tiene 4 años'
        valor_actual = evaluar(9, 3, 2020)
        self.assertEqual(valor_esperado, valor_actual)
        
    def test1948Junio14(self):
        valor_esperado = 'Usted tiene 74 años'
        valor_actual = evaluar(14, 6, 1948)
        self.assertEqual(valor_esperado, valor_actual)
    
    

if __name__ == '__main__':
    unittest.main()
