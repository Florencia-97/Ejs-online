import re

class Ejercicio:

    def __init__(self, tema, ej, seccion):
        self.tema = tema
        self.ej = ej
        self.seccion = seccion
        self.consola_display = 'none'
        self.result = ""

    def setear_resultado(self, result_run):
        self.result = self.formatear_salida(result_run)
    
    def formatear_salida(self, salida):
        salida = _chequear_tiempo(salida)
        salida = salida.replace('\n','<br>')
        salida = re.sub(r'(Traceback \(most recent call last\):)', '', salida)
        salida = re.sub(r'(\(__main__.[\w]*\))', ' ', salida)
        salida = re.sub(r'(File ".\/(\w)*.py",)', 'In ', salida)
        salida = re.sub(r'(FAIL: test_[\w\s\(\.\)]*)', '<span id="error">'+ r'\1' + '</span>', salida)
        salida = re.sub(r'(FAIL(ED)?)', '<span id="rojo">' + r'\1' + '</span>', salida)
        salida = re.sub(r'(ok)', '<span id="verde">' + r'\1' + '</span>', salida)
        salida = re.sub(r'(ERROR)', '<span id="rojo">' + r'\1' + '</span>', salida)
        salida = re.sub(r'([\w]*Error)', '<span id="funcion">' + r'\1' + '</span>', salida)
        salida = re.sub(r'(OK)', '<span id="verde">' + 'Pasaste todas las pruebas!' + '</span>', salida)
        salida = re.sub(r'(test_\w*)', '<span id="funcion">'+ r'\1' + '</span>', salida)
        return salida
    
    def mostrar_consola(self):
        self.consola_display = 'visible'


def _chequear_tiempo(salida):
        if "TimeoutExpires exception" == salida:
            cad = "Tu función tardó más de lo esperado! Suele deberse esto a un ciclo infinito dentro de esta."
            cad += " Si tenés un ciclo while o for, el problema suele encontrarse allí!"
            return cad
        return salida