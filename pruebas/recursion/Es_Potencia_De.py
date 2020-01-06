# def es_potencia_de(a,b):

class TestStringMethods(unittest.TestCase):

    def test_potencia_y_base_positiva_pos(self):
        msg = "25 es potencia de 5"
        self.assertTrue(es_potencia_de(25,5), msg)
    
    def test_potencia_y_base_positiva_neg(self):
        msg = "9 no es potencia de 5"
        self.assertFalse(es_potencia_de(9,5), msg)

    def test_potencia_y_base_negativa_pos(self):
        msg = "-8 es potencia de -2"
        self.assertTrue(es_potencia_de(-8,-2), msg)

    def test_potencia_y_base_negativa_no(self):
        msg = "-7 no es potencia de -2"
        self.assertFalse(es_potencia_de(-7,-2), msg)

    def test_base_nula(self):
        msg = "0 no es base de ningún de 10"
        self.assertFalse(es_potencia_de(10,0), msg)


if __name__ == '__main__':
    unittest.main()
