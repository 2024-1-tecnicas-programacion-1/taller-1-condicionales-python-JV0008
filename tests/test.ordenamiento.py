import sys
from pathlib import Path
import unittest
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
        
    def testNo2(self):
        valor_esperado = "30 49 100 132"
        valor_actual = evaluar(49, 30, 132, 100)
        self.assertEqual(valor_esperado, valor_actual)
        
    def testNo3(self):
        valor_esperado = "4 5 15 30"
        valor_actual = evaluar(15, 30, 4, 5)
        self.assertEqual(valor_esperado, valor_actual)
        
    def testNo4(self):
        valor_esperado = "0.2 0.4 2.1 30.3"
        valor_actual = evaluar(0.2, 30.3, 0.4, 2.1)
        self.assertEqual(valor_esperado, valor_actual)


if __name__ == '__main__':
    unittest.main()