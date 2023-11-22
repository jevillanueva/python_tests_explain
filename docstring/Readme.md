# Docstring
Los comentarios declarados en la primera línea con comillas """""" corresponden a los docs generados y pueden ser visualizados 
mediante el atributo \_\_doc\_\_ en el objeto python pueden declararse en 
- el modulo
- clases
- funciones
y otros más

Desde terminal puede visualizarse ingresando a python interactivo
```sh
cd docstring
python
```
```py
from sample import palindromo
palindromo.__doc__
```
o mediante
```
help(palindromo)
```

También podemos visualizar  todo el módulo y los atributos que lo componen
```sh
cd docstring
python
```
```py
import sample
sample.__doc__
sample.User.__doc__
sample.User.__init__.__doc__
help(sample.User.__init__)
```
# Doctest
También se puede ejecutar pruebas utilizando los Examples declarados en nuestro código python o utilizar un archivo test_<nombremodulo>.txt que contiene los ejemplos utilizando
la librería **doctest**, el formato en los examples esta en el mismo formato que la terminal interactiva de python con 3 signos mayor que ">>>"
utilizando la terminal:
```sh
cd docstring
python -m doctest sample.py
# para poder visualizar utilizamos el argumento -v
python -m doctest sample.py -v
```
Para ejecutar los tests mediante el archivo txt utilizaremos el archivo test_sample.txt
```sh
cd docstring
python -m doctest test_sample.txt 
# para poder visualizar utilizamos el argumento -v
python -m doctest test_sample.txt -v
```

> Esta parte para abajo es la misma en ingles la uso para practicar mi escritura lo siento si hay errores de sintaxis y ortográficos
> This section is the same using English lang, I can use for practice my writing, I'm so sorry for syntax and orthographic errors

# Docstring
The comments declared how to docstring will be on the first line with double quote mark """""", it can visualized using the attrib \_\_doc\_\_ in the object, the docstring can declare at
- module
- class
- function
and other more.

From terminal we can visualize using python interactive
```sh
cd docstring
python
```
```py
from sample import palindromo
palindromo.__doc__
```
or using
```
help(palindromo)
```
Also, we can visualize docs in module and its attributes
```sh
cd docstring
python
```
```py
import sample
sample.__doc__
sample.User.__doc__
sample.User.__init__.__doc__
help(sample.User.__init__)
```
# Doctest
We can execute tests using the examples declared in the docstring or use other file "test_<name>.txt" that contain the examples, for both cases using the library  **doctest**, the format used in the examples
is the same format that the python interactive using 3 sign greater than ">>>"
using the terminal:
```sh
cd docstring
python -m doctest sample.py
# for visualize the execution usign the argument -v
python -m doctest sample.py -v
```
For execute the tests using the txt file "test_sample.txt"
```sh
cd docstring
python -m doctest test_sample.txt 
# para poder visualizar utilizamos la etiqueta -v
python -m doctest test_sample.txt -v
```