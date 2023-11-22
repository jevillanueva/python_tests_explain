"""Este es el Docstring del módulo."""

# #Docstring
# #__doc__

class User:
    """Permite representar un usuario."""

    def __init__ (self, username: str, password: str) -> None:
        """Inicializa un usuario.
        
        Args:
            username: nombre de usuario
            pass: contraseña del usuario
        """
        self.username = username
        self.password = password

def palindromo (sentence: str) -> bool:
    """Permite conocer si un string es palíndromo o no.
    
    Args:
        sentence: string

    Returns:
        bool

    Examples:
        >>> palindromo('Anita lava la tina')
        True
        >>> palindromo('Hola mundo')
        False
        >>> sentence = 'Oso'
        >>> palindromo(sentence)
        True
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]

def palindromo2 (sentence: str) -> bool:
    """Permite conocer si un string es palíndromo o no v2.
    Args:
        sentence: string
    Returns:
        bool
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]