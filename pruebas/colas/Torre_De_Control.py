# class TorreDeControl:

import queue

class TestStringMethods(unittest.TestCase):

    def test_torre_de_control_vacia(self):
        torreDeControl = TorreDeControl()
        self.assertEqual(torreDeControl.asignar_pista(), "no hay vuelos en espera")
    
    def test_torre_de_control_con_vuelos(self):
        torreDeControl = TorreDeControl()
        torreDeControl.nuevo_arribo("AR156")
        self.assertEqual(torreDeControl.ver_estado(), "Vuelos esperando para aterrizar: AR156")

if __name__ == '__main__':
    unittest.main()
