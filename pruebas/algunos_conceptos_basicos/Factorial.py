# def factorial(n):

class TestFactorial(unittest.TestCase):

    def test_factorial_cero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_uno(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_cuatro(self):
        self.assertEqual(factorial(4), 24)

    def test_factorial_doce(self):
        self.assertEqual(factorial(12), 479001600)

if __name__ == '__main__':
    unittest.main()