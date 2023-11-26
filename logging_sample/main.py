import logging

#DEBUG      = 10 = debug
#INFO       = 20 = info
#WARNING    = 30 = warning
#ERROR      = 40 = error
#CRITICAL   = 50 = critical

logging.basicConfig(level=logging.DEBUG,
                    format="%(process)s-%(processName)s-%(thread)s-%(threadName)s-%(levelname)s-%(asctime)s-%(message)s)",
                    datefmt="%Y/%m/%d",
                    filename="logging_sample.log",
                    filemode="w"
                    )
def suma(a: int, b: int) -> int:
    """Suma de dos números.

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: Resultado de la suma.
    """
    logging.debug('Antes de la suma')
    c = a + b
    logging.debug('Después de la suma')
    return c

if __name__ == '__main__':
    logging.debug('Antes del llamado de la función')
    resultado = suma(10, 20)
    logging.info(resultado)