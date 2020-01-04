# def lista_ordenada(lista):

class TestStringMethods(unittest.TestCase):

    def test_lista_no_ordenada(self):
        self.assertFalse(lista_ordenada([1,3,2]), 'La lista [1,3,2] no está ordenada')

    def test_lista_ordenada(self):
        self.assertTrue(lista_ordenada([1,2,3]), 'La lista [1,2,3] está ordenada')

    def test_lista_vacia_esta_ordenada(self):
        self.assertTrue(lista_ordenada([]), 'Una lista vacia está ordenada')

if __name__ == '__main__':
    unittest.main()