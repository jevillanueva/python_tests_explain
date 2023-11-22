def sum_dos_numeros_positivos(a: int, b: int) -> int:
    """
    Suma dos números enteros positivos

    Args:
        a (int): Primer numero
        b (int): Segundo numero

    Returns:
        int: Suma de los dos números
    """
    assert a > 0 and b > 0, "Los números deben ser positivos"
    return a + b


if __name__ == '__main__':
    resultado = sum_dos_numeros_positivos(20, 20)
    print (resultado)
    resultado = sum_dos_numeros_positivos(-20, 20)
    print (resultado)