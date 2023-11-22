# Estructura para un proyecto
Cuando se trata de un proyecto tiene que existir orden y un ejemplo seria este proyecto donde el mismo proyecto de unittesting
se encuentra ahora con un formato de paquetes y separado en directorios con una estructura básica con los archivos \_\_init\_\_.py para declarar paquetes
dentro de models y de tests

root
-> models
    -> product.py
    -> shopping_cart.py
    -> test
        -> test_shopping_cart
        -> test_product
-> main.py

La ejecución de los test en la terminal:
```sh
cd project_sample
python -m unittest models.test.test_shopping_cart -v 
python -m unittest models.test.test_product -v 
```

En caso de tener multiples clases de tests y si se quiere ejecutar solo un grupo de tests ejecutar en la terminal:
```sh
cd project_sample
python -m unittest models.test.test_shopping_cart.TestShoppingCart -v
python -m unittest models.test.test_shopping_cart.TestShoppingCart2 -v
```

También se puede ejecutar tests específicos detallando en la ejecución
```sh
cd project_sample
python -m unittest models.test.test_shopping_cart.TestShoppingCart.test_product_object -v
python -m unittest models.test.test_shopping_cart.TestShoppingCart2.test_example -v
```

Para ejecutar todos los test de forma global se debe utilizar discover donde ejecutará todas las pruebas 
```sh
cd project_sample
python -m unittest discover
```
