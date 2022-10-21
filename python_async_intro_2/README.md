### ejercicio

Tenemos un servidor en [async_service/sync_server.py](async_service/sync_server.py) que expone un servicio crítico para nuestra empresa: dado un número, calcula su cuadrado eg.

`GET /calculate_square?num=2`

nos devolvería un string:

```
4.0
```

Por desgracia, el código es síncrono, nuestra empresa hace cada vez más llamadas al servicio, y se está convirtiendo en un cuello de botella para nuestras operaciones.

Uno de nuestros empleados ha creado un script llamado [async_service/test_script.py](async_service/test_script.py) que ilustra el problema lanzando 4 queries concurrentes: si lanzamos un servidor en `localhost:8888` con `env/bin/python -m async_service.sync_server` y lanzamos 4 queries concurrentes con el script de prueba, vemos que todo el proceso tarda más de 4 segundos:

```
miguelsimon$ time env/bin/python -m async_service.test_script
[0.0, 1.0, 4.0, 9.0]

real	0m4.456s
user	0m0.346s
sys	0m0.143s
```

Tras pagar cantidades ingentes de dinero al consultor que programó el backend que calcula los cuadrados, este nos ha proporcionado una versión asíncrona en [async_service/async_backend.py](async_service/async_backend.py). Nos ha dicho que no puede optimizar más allá de 1 segundo el proceso de calcular un cuadrado en una consulta individual, pero que sí que podemos lanzar varias consultas en paralelo si usamos la versión asíncrona del backend.


#### pregunta 1

El script de prueba [async_service/test_script.py](async_service/test_script.py) está programado de forma síncrona usando requests y usa [ProcessPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) para gestionar la concurrencia.

¿Puedes escribir una versión del script llamada `async_service/async_test_script.py` que tenga el mismo comportamiento pero que use [asyncio](https://docs.python.org/3/library/asyncio.html) para gestionar la concurrencia en vez de [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)?

Posibilidades:

* usar una librería http asíncrona como [aiohttp](https://docs.aiohttp.org/en/stable/)
* usar [tornado.httpclient](https://www.tornadoweb.org/en/stable/httpclient.html)

#### pregunta 2

¿Puedes escribir una versión asíncrona del servidor llamada `async_service/async_server.py` que use [async_service/async_backend.py](async_service/async_backend.py) para poder servir múltiples clientes de forma concurrente?

El output de `async_service.test_script` contra esta versión del server debería tardar ~1 segundo en vez de ~4 segundos, eg.

```
miguelsimon$ time env/bin/python -m async_service.test_script
[0.0, 1.0, 4.0, 9.0]

real	0m1.456s
user	0m0.346s
sys	0m0.143s
```

#### pregunta 3

Ahora el servidor puede estar procesando varias llamadas en cada momento: queremos añadir un endpoint `GET /list_current_jobs` que nos responda (en json) con los cuadrados que están siendo calculados por el servidor en ese momento.

Por ejemplo, si llamásemos `GET /list_current_jobs` justo después de lanzar `async_service.test_script`, esperaríamos una respuesta de este estilo (el orden no tiene porqué estar definido):

`GET /list_current_jobs`

```json
[2, 3, 0, 1]
```

## usage

### install

```
python3 -m venv env
env/bin/pip install -r requirements.txt
```

### run test_script

Launch the server in a terminal window, it should listen on `localhost:8888`:

```
env/bin/python -m async_service.sync_server
```

You can launch the test script in another window:

```
time env/bin/python -m async_service.test_script
```

### run tests

```
env/bin/python -m unittest discover .
```
