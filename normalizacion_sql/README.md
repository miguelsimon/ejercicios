Hemos tocado el tema de la [normalización de base de datos](https://en.wikipedia.org/wiki/Database_normalization) y me ha dado la impresión de que igual vendría bien un repaso.

Un buen diseño de schema de datos es extremadamente importante; una tarea que lleva segundos con un buen schema puede llevar horas (o ser imposible de realizar) con un mal schema.

Tampoco tenemos que empezar a demostrar teoremas de teoría de conjuntos como Date y Codd, pero vamos a hacer lo siguiente:

1) Leer la entry de la wiki
2) Solucionar el siguiente ejercicio, cada uno por su lado, usando `sqlite3` para hacer pruebas
3) El viernes en la daily presentamos soluciones y las comentamos @jmartinezpoq, @dorogoy y @valentinboyanov

### Ejercicio

Un veterinario de Valencia te ha pedido ayuda con la base de datos que usa para guardar sus clientes.

Actualmente, usa la siguiente base de datos (cortar y pegar en línea de comandos de [sqlite](https://www.sqlite.org/index.html)); algo le incomoda de mantener los nombres de las mascotas en una lista separada por comas, pero hasta ahora ha funcionado:

```sql
create table people (
  dni varchar primary key,
  firstname varchar,
  lastname varchar,
  address_1 varchar,
  address_2 varchar,
  pet_names varchar
);

insert into
  people(dni, firstname, lastname, address_1, pet_names)
  values("93434423F", "isaac", "newton", "lauria 27, valencia", "paul,polly,peter");

insert into
  people(dni, firstname, lastname, address_1)
  values("73434423F", "e.t.", "jaynes", "lauria 28, valencia");

insert into
  people(dni, firstname, lastname, address_1, address_2, pet_names)
  values("53434423F", "george", "polya", "colon 01, valencia",  "tapineria 33, betera", "pepe");
```

Pero ahora se encuentra con un problema; E.T. Jaynes le ha traído a Madonna como clienta, que presenta varias dificultades, entre ellas que tiene 3 residencias distintas; ha apuntado los datos en una servilleta provisionalmente mientras espera a que cambies el diseño de la base de datos para acomodarla:

```
dni: "23434423F"
Madonna
address 1: "cajal 3, macastre"
address 2: "lauria 33, paterna"
address 3: "colon 45, valencia"
pet names: killer,hunter
```

1) Cambiar el diseño de la base de datos a algo más sensato
2) Escribir el nuevo schema y los inserts necesarios para que se puedan cortar y pegar en una sesión de línea de comandos de sqlite3
