* [Ejercicio](#Ejercicio)
  * [Pregunta 0](#Pregunta-0)
  * [Pregunta 1](#Pregunta-1)
  * [Pregunta 2](#Pregunta-2)
* [Herramientas conceptuales](#Herramientas-conceptuales)
* [Herramientas de implementación](#Herramientas-de-implementación)
* [Presentación de soluciones](#Presentación-de-soluciones)

<a title="Hugovanmeijeren, CC BY-SA 3.0 &lt;https://creativecommons.org/licenses/by-sa/3.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Cern_datacenter.jpg"><img width="512" alt="Cern datacenter" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Cern_datacenter.jpg/512px-Cern_datacenter.jpg"></a>

## Ejercicio

Tenemos que llevar a cabo una tarea de limpieza en un bucket que contiene un montón de archivos.

Antes de lanzarnos a lidiar con el bucket, vamos a resolver el problema en local con un conjunto de datos de prueba: lo haremos de forma que nuestra solución sea escalable a conjuntos de datos de petabytes con poco esfuerzo, usando [google Dataflow](https://cloud.google.com/dataflow).

Los archivos son de tipo gzip, generados automáticamente por sistemas de control que chequean periódicamente la integridad de otros sistemas.

Nos hemos dado cuenta que el sistema que los genera ha introducido un bug, y en algunos archivos hay una inconsistencia entre los metadatos contenidos en los nombres del archivo y los metadatos contenidos en el archivo en sí.

Los nombres de los archivos tienen la estructura `{nombre_de_check}-{iso_timestamp}.tar.gz`, eg. `check_200-2021-08-16T02:46:39.003135.tar.gz`.

Cada uno de estos archivos contiene un directorio comprimido con la siguiente estructura:

```
├── metadata.json
└── result.json
```

El archivo `metadata.json` contiene metadatos que deberían coincidir con los metadatos que son parte del nombre del fichero, eg.

```json
{"check_name": "check_200", "stamp": "2021-08-16T02:46:39.003135"}
```

Pero en algunos casos el sistema ha escrito mal el `check_name` en el fichero `metadata.json`. **El nombre contenido en el nombre del archivo siempre es correcto**.

Queremos detectar los archivos con datos inconsistentes y seguidamente corregir aquellos archivos que tengan un formato erróneo.


### Pregunta 0

Para el directorio [./blobs](./blobs):

Escribir un programa en python puro, lo más sencillo posible, que arregle los archivos, dejando la colección correcta en el directorio [./clean_blobs_1](./clean_blobs_1).

### Pregunta 1

Escribir un programa que haga exactamente lo mismo, pero usando [apache Beam](https://beam.apache.org/) y dejando los resultados en [./clean_blobs_2](./clean_blobs_2).

Esto consiste en expresar el problema en términos de PCollections y de PTransforms, un proceso que puede ser algo tedioso y requerirá bucear en los docs.

Si expresamos el programa usando apache beam, podemos usar su runner para [google Dataflow](https://cloud.google.com/dataflow) y escalar trivialmente a miles de instancias.

### Pregunta 2

En condiciones reales, los archivos residen en un bucket de [google cloud storage](https://cloud.google.com/products/storage/) y hay petabytes de ellos: ¿cómo habrá que modificar la solución a la pregunta 2 para que el source y el sink sean buckets de google cloud en vez de archivos en local?

¿Cómo hay que diseñar el código para poder cambiar de source y sink fácilmente?

## Herramientas conceptuales

[Mapreduce](https://en.wikipedia.org/wiki/MapReduce) es un nombre para una familia de técnicas para particionar problemas y resolverlos en clusters en paralelo.

## Herramientas de implementación

[Beam](https://beam.apache.org/): tiene un runner para [google Dataflow](https://cloud.google.com/dataflow), cosa que simplificará mucho nuestro trabajo.

También podríamos usar [spark](https://spark.apache.org/), que es conceptualmente casi idéntico; la diferencia es que tendríamos que administrar nosotros el cluster de spark, y en el caso de beam + Dataflow podemos delegar todo ese tedio a google.

NB. estas herramientas son de última generación y también permiten expresar operaciones en streaming: nosotros por ahora nos vamos a limitar a implementar operaciones sencillas en batch.

El módulo [tarfile](https://docs.python.org/3/library/tarfile.html) de python.

## Presentación de soluciones

Como siempre, se hacen forks del repo y cada uno commitea su solución en su fork para luego presentarlas en común; nos esperamos a subirlas hasta el día de presentación de resultados para no condicionar las soluciones de los demás.
