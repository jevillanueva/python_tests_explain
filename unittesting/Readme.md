# Unittest
Assert = Evaluar condición, si se cumple el programa continua, si no se cumple termina le ejecución con error
Utilizando "sample.py" desde la terminal
```sh
cd unittesting
python sample.py
```
Otro ejemplo del uso de assert se puede ver en el ejemplo dos para validar números positivos
```sh
cd unittesting
python sample2.py
```

## Libreria unittest
Para hacer uso de la libreria unittest primero se debe importar y definir una clase que herede de testcase, es una buena practica empezar las clases conn el prefijo Test dentro de esta los métodos que serán definidos tienen que empezar con el prefijo "test_" para que puedan ser encontrados y ejecutados
```sh
cd unittesting
python sample3.py
# para mas detalles usar el argumento -v 
python sample3.py -v
```
Otro ejemplo para objetos son los realizados con los siguientes módulos
- product.py
- shopping_cart.py
- test_shopping_cart.py

Donde se puede visualizar en el test la creación de los objetos, y la definición de los métodos "setUp" y "tearDown" que se ejecutan antes de cada test, y los métodos setUpClass y tearDownClass que se ejecutan antes de todos los test 1 sola vez y al terminar todas las ejecuciones.
En este se puede encontrar 
- assertEqual -> Compara si son iguales
- assertTrue, assertFalse -> Compara si el resultado es Verdadero o si es Falso
- assertIn, assertNotIn -> Compara si un objeto existe en otro, o si el objeto no existe en otro
- assertRaises -> Compara si se ejecuta correctamente las Excepciones
- assertGreater, assertLesser -> Compara si el valor es mayor que o si es menor que
- assertGreaterEqual, assertLesserEqual -> Compara si el valor es mayor o igual que o menor o igual que

Se puede saltar tests de 3 Formas diferentes
- skip -> Salta automáticamente el test
- skipIf -> Salta las pruebas si cumplen una condición (true)
- skipUnless -> Salta la pruebas si no cumplen la condición (false)

Expresiones regulares se pueden encontrar en las pruebas unitarias
- assertRegex -> Se puede validar expresiones regulares y también buscar un substring dentro un string como en el ejemplo en 
el "archivo test_shopping_cart.py"

```sh
cd unittesting
python test_shopping_cart
# para mas detalles usar el argumento -v 
python test_shopping_cart -v
```
