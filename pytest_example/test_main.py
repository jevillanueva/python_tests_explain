import pytest


def test_example():
    assert 10 == 10, "La prueba no ha pasado"


class TestExample:
    @classmethod
    def setup_class(cls):
        print(">> Antes de todas la pruebas")

    @classmethod
    def teardown_class(cls):
        print(">> Después de todas la pruebas")

    def setup_method(self):
        print("Iniciando test")
        self.numero_uno = 10
        self.numero_dos = 5

    def teardown_method(self):
        print("Finalizando test")

    def test_suma_dos_numeros(self):
        assert self.numero_uno + self.numero_dos == 15, "La suma no es correcta"

    def test_resta_dos_numeros(self):
        assert self.numero_uno - self.numero_dos == 5, "La resta no es correcta"


class TestExample2:
    def test_multiplicacion_dos_numeros(self):
        assert 10 * 10 == 100, "La multiplicación no es correcta"
