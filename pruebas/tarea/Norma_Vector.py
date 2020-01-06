# def norma(x, y, z):

class TestTarea1(unittest.TestCase):

    def test_norma_con_valor_negativo(self):
        self.assertAlmostEqual(norma(3,2,-4),  5.385164807134504)

    def test_norma_punto_origen(self):
        self.assertAlmostEqual(norma(0,0,0), 0)


if __name__ == '__main__':
    unittest.main()