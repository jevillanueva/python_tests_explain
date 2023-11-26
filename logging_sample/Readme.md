# Logging
Para un control de la ejecución es importante tener el registro de lo que sucede en la ejecución para esto es útil el módulo logging
Existen varios niveles de logging y su prioridad.

- DEBUG      = 10
- INFO       = 20
- WARNING    = 30
- ERROR      = 40
- CRITICAL   = 50

Por defecto tiene configurado un nivel de prioridad 30 por lo cual INFO y DEBUG están omitidos por default
para modificar el comportamiento por default se debe utilizar "logging.basicConfig" para definir que nivel de prioridad se visualizará

Para modificar el formato del logging se tienen como ejemplo los siguientes campos

- %(process)s       => Id del proceso
- %(processName)s   => Nombre del proceso
- %(thread)s        => Id del thread
- %(threadName)s    => Nombre del thread
- %(levelname)s     => Tipo de mensaje
- %(message)s       => El mensaje a imprimir por el logging
- %(asctime)s       => Format de la fecha YYYY-MM-DD HH:mm:ss,SSS (ISO 8601)*

* Para modificar el formato de la fecha se utiliza el atributo "datefmt" donde se puede cambiar el formato de la fecha

Los logging pueden ser almacenados en un archivo y se debe configurar en  "basicConfig"
con los atributos "filename" donde va el nombre del archivo a generar los logs y "filemode" para decidir como se traba el archivo
- filemode="a"   => adiciona al final del archivo los logs. Si no existe el archivo se crea
- filemode="w"   => Abre el archivo trunca el contenido y escribe el nuevo log. Si no existe el archivo se crea
- filemode="x"   => Si no existe el archivo se crea, Si existe un archivo falla la ejecución
- filemode="r"   => El archivo es de solo lectura no se escribirán logs.

```sh
cd logging_sample
python main.py
```