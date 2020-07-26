* [Ejercicio](#ejercicio)
  * [Pregunta 1](#pregunta-1)
  * [Pregunta 2](#pregunta-2)
  * [Pregunta 3](#pregunta-3)
  * [Pregunta 4](#pregunta-4)
* [Herramientas conceptuales](#herramientas-conceptuales)
* [Herramientas de implementación](#herramientas-de-implementación)
* [Presentación de soluciones](#presentación-de-soluciones)

![casino_royale](casino_royale.jpg)

### Ejercicio

**Dimensionado de servidores**

Tenemos una empresa que diseña bombas de agua. Como parte de su trabajo, los analistas de vez en cuando tienen que ejecutar [simulaciones de FEA](https://en.wikipedia.org/wiki/Finite_element_method) complejas, que ejecutan como jobs en nodos de computación de un proveedor de cloud.

Los nodos de computación:
* se reservan al día con la siguiente estructura de pricing
  * un nodo vale 130 euros/día
  * a partir de 2 nodos reservados, nos hacen un descuento por volumen y cada nodo adicional vale 110 euros/día
* cada nodo tiene capacidad para procesar 72 horas-cpu al día

Ej. si en un día reservamos 3 nodos, nos cobran `130 + 130 + 110` euros.

La empresa tiene 14 analistas en plantilla; hemos mirado el histórico, y hemos determinado que la probabilidad de que un analista tenga que ejecutar una simulación de FEA en un día dado es de `0.156`.

También mirando el histórico, nos hemos dado cuenta que los requisitos de horas-cpu por job de FEA siguen una [distribución uniforme](https://en.wikipedia.org/wiki/Uniform_distribution_(continuous)): un job necesita entre 15.7 y 33.1 horas-cpu de computación.

#### Pregunta 1

¿Cuánto es el máximo que podemos llegar a pagar en un día por los servidores?

#### Pregunta 2

Pinta un histograma de la distribución de los costes diarios realizando simulaciones de Monte Carlo.

¿Cuál es el coste medio por día que esperamos tener que pagar por los servidores, si siempre pagamos todos los servidores que hacen falta en un día dado?

#### Pregunta 3

Supongamos que siempre pagamos todos los servidores que hacen falta en un día dado.

Pinta un histograma de la distribución de los gastos semanales realizando experimentos de Monte Carlo.

¿Cuál es la probabilidad que el gasto en una semana laborable (5 días) supere los 900 euros?

#### Pregunta 4

El departamento de contabilidad exige que cerremos el presupuesto diario por adelantado.

No podemos pagar suficiente para **garantizar** que **nunca** se quede nadie sin servicio.

Hemos decidido que es aceptable si en un día dado la probabilidad de que acaben todos los jobs es como mínimo del 90%.

¿Cuánto es lo mínimo que tenemos que pagar al día para tener una probabilidad como mínimo del 90% de tener capacidad para todos los jobs?

### Herramientas conceptuales

Este ejercicio es una introducción a los [métodos de Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method). Estamos analizando datos univariados como en [el ejercicio anterior](../datos_univariados_1), solo que esta vez estos datos los estamos generando nosotros vía simulaciones de Monte Carlo.

Ver [intro.ipynb](intro.ipynb) con explicación y ejercicios introductorios.

Los métodos de Monte Carlo son tremendamente útiles sobre todo para los programadores, ya que hay preguntas que son muy fáciles de responder programando simulaciones sencillas pero muy difíciles de responder de forma analítica: si ya sabes programar tienes más de la mitad del trabajo hecho.

Adicionalmente, revisar:

* [concepto de esperanza](https://en.wikipedia.org/wiki/Expected_value)
* [concepto de percentil](https://en.wikipedia.org/wiki/Percentile)

### Herramientas de implementación

Seguimos con el stack científico de python: jupyter, numpy, matplotlib etc.

numpy dispone de generadores aleatorios convenientes que simplifican mucho este tipo de trabajos, por ejemplo [numpy.random.binomial](https://numpy.org/doc/stable/reference/random/generated/numpy.random.binomial.html)

### Presentación de soluciones

Como la vez anterior, se hacen forks del repo y cada uno commitea su solución en su fork para luego presentarlas en común:
* modificando `intro.ipynb` para los ejercicios de calentamiento
* la solución al ejercicio va en `solution.ipynb`
