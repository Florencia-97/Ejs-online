# def lista_tuplas_a_dic(lista_tuplas):

class TestStringMethods(unittest.TestCase):

    def test_lista_vacia(self):
        self.assertEqual(lista_tuplas_a_dic([]), {})

    def test_claves_repetidos(self):
        self.assertEqual(lista_tuplas_a_dic([(1,2),(1,4),(2,7)]), {1: [2, 4], 2: [7]})

    def test_claves_no_se_repiten(self):
        self.assertEqual(lista_tuplas_a_dic([(1,2),(5,4),(2,7)]), {1: [2], 5:[4], 2: [7]})


if __name__ == '__main__':
    unittest.main()