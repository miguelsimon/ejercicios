Para este ejercicio, revisar:
* [el concepto de una transacción](https://en.wikipedia.org/wiki/Database_transaction)
* [with statement](https://docs.python.org/3/whatsnew/2.6.html#pep-343-the-with-statement), el mecanismo de context management de python
* [los context managers son una buena forma de gestionar transacciones](https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager)

### ejercicio

Estamos a cargo del backend de una empresa que copia el modelo de [Bizum](https://bizum.es/en/): permite hacer transferencias de dinero entre usuarios.

Nuestro backend está escrito en sqlite y además no usa multithreading, así que su comportamiento debería ser fácil de analizar. Tenemos una cobertura de tests unitarios decente:

```bash
python3 -m unittest discover backend
```

Pese a que todo parece sencillo y normal, observamos de vez en cuando un comportamiento raro: hay quejas de usuarios que mandan dinero que nunca llega a su destino. El dinero sí que desaparece de la cuenta del usuario que lo envía y nos acusan de robárselo.

Hemos observado que el número de quejas de este tipo está muy correlado con los apagones de luz. Nuestro CTO decidió ahorrar costes, y nuestro server de backend está hospedado en un datacenter que regularmente sufre interrupciones en el suministro eléctrico.

Nuestro CTO también decidió ahorrar al contratar programadores, y la verdad es que ninguno sabe mucho de SQL pero a uno le suena que había un concepto llamado **transacción** que igual tenía que ver con el comportamiento observado.

Creemos que el problema se encuentra en la función `savings_backend.transfer(conn, user_a, user_b, transfer_amount)`

#### pregunta 1

¿Qué crees que está pasando?

#### pregunta 2

¿Cómo reescribirías la función `savings_backend.transfer(conn, user_a, user_b, transfer_amount)` para eliminar el bug sin tener que cambiar a un datacenter bueno?

Asegúrate de que sigue pasando los tests unitarios con `python3 -m unittest discover backend`
