import sys
from pathlib import Path
import unittest
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
        
    def test2(self):
        valor_esperado = "Inválido"
        valor_actual = evaluar(3, 7)
        self.assertEqual(valor_esperado, valor_actual)
        
    def test3(self):
        valor_esperado = "Ganó A"
        valor_actual = evaluar(7, 6)
        self.assertEqual(valor_esperado, valor_actual)
        
    def test4(self):
        valor_esperado = "Aún no termina"
        valor_actual = evaluar(5, 6)
        self.assertEqual(valor_esperado, valor_actual)
        
    def test5(self):
        valor_esperado = "Ganó B"
        valor_actual = evaluar(5, 7)
        self.assertEqual(valor_esperado, valor_actual)
        
    def test6(self):
        valor_esperado = "Inválido"
        valor_actual = evaluar(8, 6)
        self.assertEqual(valor_esperado, valor_actual)
        
    def test7(self):
        valor_esperado = "Ganó A"
        valor_actual = evaluar(6, 4)
        self.assertEqual(valor_esperado, valor_actual)
        
    def test8(self):
        valor_esperado = "Aún no termina"
        valor_actual = evaluar(2, 5)
        self.assertEqual(valor_esperado, valor_actual)
    
    

if __name__ == '__main__':
    unittest.main()

