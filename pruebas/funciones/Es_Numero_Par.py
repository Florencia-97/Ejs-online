# def es_numero_par(n):

class TestStringMethods(unittest.TestCase):

    def test_cero_es_par(self):
        msg = "0 es un número par"
        self.assertTrue(es_numero_par(0), msg)

    def test_numero_par(self):
        msg = "2 es un número par"
        self.assertTrue(es_numero_par(2), msg)

    def test_numero_impar(self):
        msg = "5 es un número impar"
        self.assertFalse(es_numero_par(5), msg)


if __name__ == '__main__':
    unittest.main()