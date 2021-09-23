* [Ejercicio](#Ejercicio)
  * [Pregunta 0](#Pregunta-0)
  * [Pregunta 1](#Pregunta-1)
* [Herramientas conceptuales](#Herramientas-conceptuales)
* [Herramientas de implementación](#Herramientas-de-implementación)
* [Presentación de soluciones](#Presentación-de-soluciones)

<a title="Hugovanmeijeren, CC BY-SA 3.0 &lt;https://creativecommons.org/licenses/by-sa/3.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Cern_datacenter.jpg"><img width="512" alt="Cern datacenter" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Cern_datacenter.jpg/512px-Cern_datacenter.jpg"></a>

## Ejercicio

Tenemos que construir un [índice invertido](https://en.wikipedia.org/wiki/Inverted_index) para los documentos en el directorio [./input_files](./input_files).

Un índice invertido hace fácil encontrar todos los documentos que contienen un término: si por ejemplo tenemos 2 ficheros con los siguientes contenidos:

* 1.txt: `Pepe y paco.`
* 2.txt: `Paco alone.`

un índice invertido asociará cada término a los archivos que lo contienen, por ejemplo, usando una línea por término.

```
alone 2.txt
paco 1.txt 2.txt
pepe 1.txt
y 1.txt
```

Cuando construyamos nuestro índice invertido *normalizaremos* el texto: pasaremos todas las letras a lowercase y descartaremos puntuación.

### Pregunta 0

Para el directorio [./input_files](./input_files):

Escribir un programa en python que emita un fichero donde cada línea contenga un término y una lista de archivos en los que aparece, todos separados por espacios.

Tanto los términos como las listas de archivos asociadas a cada término deberán estar ordenadas alfabéticamente.

Debería dar un output parecido (o idéntico) a [./index.txt](./index.txt).

### Pregunta 1

Escribir un programa que haga exactamente lo mismo, pero usando [apache Beam](https://beam.apache.org/).

Esto consiste en expresar el problema en términos de PCollections y de PTransforms, un proceso que puede ser algo tedioso y requerirá bucear en los docs.

Si expresamos el programa usando beam Beam, podemos usar su runner para [google Dataflow](https://cloud.google.com/dataflow) y escalar trivialmente a miles de instancias.

## Herramientas conceptuales

[Mapreduce](https://en.wikipedia.org/wiki/MapReduce) es un nombre para una familia de técnicas para particionar problemas y resolverlos en clusters en paralelo.

La construcción de [índices invertidos](https://en.wikipedia.org/wiki/Inverted_index) es un problema extremadamente apto para mapreduce; la construcción y mantenimiento del índice de google impulsó muchas de las tecnologías para procesar grandes cantidades de datos en paralelo que ahora están comoditizadas.

## Herramientas de implementación

[Beam](https://beam.apache.org/): tiene un runner para [google Dataflow](https://cloud.google.com/dataflow), cosa que simplificará mucho nuestro trabajo.

También podríamos usar [spark](https://spark.apache.org/), que es conceptualmente casi idéntico; la diferencia es que tendríamos que administrar nosotros el cluster de spark, y en el caso de beam + Dataflow podemos delegar todo ese tedio a google.

NB. estas herramientas son de última generación y también permiten expresar operaciones en streaming: nosotros por ahora nos vamos a limitar a implementar operaciones sencillas en batch.

## Presentación de soluciones

Como siempre, se hacen forks del repo y cada uno commitea su solución en su fork para luego presentarlas en común; nos esperamos a subirlas hasta el día de presentación de resultados para no condicionar las soluciones de los demás.
