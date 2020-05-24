### Ejercicio

Somos esbirros de contraespionaje de Diabetisa SA, una corporación que fabrica chucherías y que compite con otro gran conglomerado alimentario, Megasucrón GmbH.

Nuestro infiltrado en Megasucrón GmbH, antes de ser identificado, torturado y eliminado por operativos de seguridad corporativa, nos advirtió que Megasucrón estaba llevando a cabo un scrapeo con bots de los precios de algunas chucherías en nuestra web; nos gustaría saber qué chucherías consideran importantes.

Hemos recopilado, para cada página de nuestra web, los datos de tiempo de presencia por visita durante 1 día: para cada visita, guardamos los segundos de permanencia en la página.

Examinando estos datos y usando la cabeza,

0. vamos a cargar los datos de csv en un formato conveniente, eg. ndarray de numpy o DataFrame de pandas
1. vamos a representar los datos gráficamente; qué representaciones nos pueden ayudar?
  * representar todo en una misma gráfica vs. en gráficas separadas?
  * cuidado con los ejes autoajustados: para comparar gráficas distintas tienen que compartir escala y límites
2. podemos identificar, a ojímetro, qué páginas están siendo scrapeadas y qué páginas no? Qué criterio usamos?
3. podemos estimar, a mano, qué número aproximado de nuestras visitas diarias se debe a bots y qué número a personas?
4. podemos escribir un programa que, dado un array de tiempos de permanencia, devuelva `True` si está siendo scrapeada y `False` en otro caso?

### Herramientas conceptuales

* El [histograma](https://en.wikipedia.org/wiki/Histogram) es la herramienta fundamental cuando te enfrentas a datos [univariados](https://en.wikipedia.org/wiki/Univariate_distribution) (y en otros casos también)
* El concepto de [moda](https://en.wikipedia.org/wiki/Mode_(statistics)), [distribuciones multimodales](https://en.wikipedia.org/wiki/Multimodal_distribution)

### Herramientas de implementación

Vamos a empezar a tomar contacto con el stack moderno de python de computación científica, todo instalable con pip:
* [jupyter notebook](https://jupyter.readthedocs.io/en/latest/install.html)
* [numpy](https://numpy.org/)
* [matplotlib](https://matplotlib.org/)
* [pandas](https://pandas.pydata.org/)

### Presentación de soluciones

Notebook es muy útil para análisis de datos porque se puede mezclar código, gráficas y texto con poco esfuerzo; la solución será un notebook que subáis a vuestro github.

Se puede commitear el notebook (.ipynb) y github tiene un visualizador que lo renderiza: hay un ejemplo básico de una interacción trivial en [example.ipynb](example.ipynb) que os puede servir como punto de partida.
