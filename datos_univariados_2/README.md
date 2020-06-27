* [Ejercicio](#ejercicio)
* [Herramientas conceptuales](#herramientas-conceptuales)
* [Herramientas de implementación](#herramientas-de-implementación)
* [Presentación de soluciones](#presentación-de-soluciones)

### Ejercicio

**Dimensionado de servidores**

Tenemos una empresa que diseña bombas de agua. Como parte de su trabajo, los analistas de vez en cuando tienen que ejecutar [simulaciones de FEA](https://en.wikipedia.org/wiki/Finite_element_method), que ejecutan como jobs en nodos de computación de un proveedor de cloud.

Los nodos de computación:
* se reservan al día con la siguiente estructura de pricing
  * un nodo vale 130 euros/día
  * a partir de 2 nodos reservados, nos hacen un descuento por volumen y cada nodo adicional vale 110 euros/día
* cada nodo puede procesar un máximo de 3 jobs de FEA en un día

Ej. si en un día reservamos 3 nodos, nos cobran `130 + 130 + 110` euros.

La empresa tiene 14 analistas en plantilla; hemos mirado el histórico, y hemos determinado que la probabilidad de que un analista tenga que ejecutar una simulación de FEA en un día dado es de `0.156`.

#### Pregunta 1

¿Cuánto es el máximo que podemos llegar a pagar en un día por los servidores?

#### Pregunta 2

¿Cuál es el coste medio por día que esperamos tener que pagar por los servidores?

#### Pregunta 3

El departamento de contabilidad exige que cerremos el presupuesto diario por adelantado, para pedir un préstamo para financiar las operaciones del mes siguiente.

No podemos pagar suficiente para garantizar que **nunca** se quede nadie sin servicio.

Hemos decidido que vamos bien si el `90%` de los diás todos los jobs de FEA encolados acaban, es aceptable que se queden jobs sin acabar en un `10%` de los días.

¿Cuánto es lo mínimo que tenemos que pagar al proveedor de cloud al día para obtener este nivel de servicio?

### Herramientas conceptuales

Este ejercicio es una introducción a los [métodos de Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method). Estamos analizando datos univariados como en [el ejercicio anterior](../datos_univariados_1), solo que esta vez estos datos los estamos generando nosotros vía simulaciones de Monte Carlo.

Ver [intro.ipynb](intro.ipynb) con explicación y ejercicios introductorios.

Los métodos de Monte Carlo son tremendamente útiles sobre todo para los programadores, ya que hay preguntas que son muy fáciles de responder programando simulaciones sencillas pero muy difíciles de responder de forma analítica: si ya sabes programar tienes más de la mitad del trabajo hecho.

Adicionalemente, revisar:

* [concepto de esperanza](https://en.wikipedia.org/wiki/Expected_value)
* [concepto de percentil](https://en.wikipedia.org/wiki/Percentile)

### Herramientas de implementación

Seguimos con el stack científico de python: jupyter, numpy, matplotlib etc.

numpy dispone de generadores aleatorios convenientes que simplifican mucho este tipo de trabajos, por ejemplo [numpy.random.binomial](https://numpy.org/doc/stable/reference/random/generated/numpy.random.binomial.html)

### Presentación de soluciones

Como la vez anterior, se hacen forks del repo y cada uno commitea su solución en su fork para luego presentarlas en común:
* modificando `intro.ipynb` para los ejercicios de calentamiento
* la solución al ejercicio va en `solution.ipynb`
