# def expresion_balanceada(exp):

class TestStringMethods(unittest.TestCase):

    def test_expresion_balanceada_corta(self):
        msg = "(x+y)/2 es una expresión balanceada"
        self.assertTrue(expresion_balanceada('(x+y)/2'), msg)

    def test_expresion_balanceada_larga(self):
        msg = "'[8*4(x+y)]+{2/5}' es una expresión balanceada"
        self.assertTrue(expresion_balanceada('[8*4(x+y)]+{2/5}'), msg)
    
    def test_expresion_no_balanceada_corta(self):
        msg = "'(x+y]/2' no es una expresión balanceada"
        self.assertFalse(expresion_balanceada('(x+y]/2'), msg)

    def test_expresion_no_balanceada_larga(self):
        msg = "'1+)2(+3' no es una expresión balanceada"
        self.assertFalse(expresion_balanceada('1+)2(+3'), msg)

if __name__ == '__main__':
    unittest.main()