Reglas como la última vez:
* cada uno intenta resolverlo de forma independiente, este viernes nos reunimos para comparar soluciones
* justo antes de la reunión pegamos nuestras soluciones en el issue para no condicionarnos

Cualquiera que quiera unirse es bienvenido, que lo diga en este issue para que le invitemos a la presentación de resultados

Para este ejercicio, revisar:
* [joins](https://en.wikipedia.org/wiki/Join_(SQL))
* [set operations](https://en.wikipedia.org/wiki/Set_operations_(SQL))
* agregación vía `group by`

#### ejercicio

Una empresa de yogures está trabajando en la creación del yogur definitivo; para ello llevan entre manos varios proyectos, que utilizan distintos recursos. Cada recurso lo lleva un departamento distinto, con su propia forma de hacer las cosas:

* La oficina de Valencia no cree en la normalización y guarda los datos de horas imputadas en una tabla, asociadas a nombres de empleados y nombres de proyecto
* La oficina de Macastre tiene una tabla de empleados, y asocia horas imputadas a id de empleado e id de proyecto
* El acelerador de partículas asocia nombres de proyectos directamente a euros

La contabilidad ha escapado a su control, y tenemos que integrar estas fuentes de datos distintas para responder a preguntas de negocio; la respuesta a cada pregunta será una tabla, creada vía un [view](https://en.wikipedia.org/wiki/View_(SQL)). Podemos crear todas las views auxiliares que queramos.

Pegar directamente en [línea de comandos de sqlite](https://www.sqlite.org/index.html):

```sql
create table proyectos (
  id int primary key,
  name varchar unique,
  description varchar not null
);

create table empleados_macastre (
  id int primary key,
  name varchar unique
);

create table horas_macastre (
  employee_id int references empleados_macastre (id),
  project_id int references proyectos (id),
  hours int not null
);

create table horas_valencia (
  employee_name varchar not null,
  project_name varchar references proyectos (name),
  hours int not null
);

create table acelerador_particulas (
  project_name varchar not null,
  euros float not null
);

create table sueldos (
  employee_name varchar primary key,
  euros_hour float not null
);

insert into empleados_macastre(id, name) values (0, 'juana juanez');
insert into empleados_macastre(id, name) values (1, 'pepe pepez');

insert into sueldos (employee_name, euros_hour) values ('juana juanez', 0.6);
insert into sueldos (employee_name, euros_hour) values ('pepe pepez', 0.75);
insert into sueldos (employee_name, euros_hour) values ('martin martinez', 0.70);
insert into sueldos (employee_name, euros_hour) values ('dr. maria lopez', 1.05);

insert into proyectos(id, name, description) values(1, 'ultrayogur', '');
insert into horas_macastre (employee_id, project_id, hours) values (0, 1, 10);
insert into horas_macastre (employee_id, project_id, hours) values (0, 1, 22);
insert into horas_macastre (employee_id, project_id, hours) values (1, 1, 5);
insert into horas_valencia (employee_name, project_name, hours) values ('martin martinez', 'ultrayogur', 18);
insert into acelerador_particulas(project_name, euros) values ('ultrayogur', 2);

insert into proyectos(id, name, description) values(2, 'megayogur', '');
insert into horas_macastre (employee_id, project_id, hours) values (1, 2, 10);
insert into horas_valencia (employee_name, project_name, hours) values ('martin martinez', 'megayogur', 6);
insert into horas_valencia (employee_name, project_name, hours) values ('dr. maria lopez', 'megayogur', 8);
insert into horas_valencia (employee_name, project_name, hours) values ('dr. maria lopez', 'megayogur', 23);
insert into acelerador_particulas(project_name, euros) values ('megayogur', 1);
insert into acelerador_particulas(project_name, euros) values ('megayogur', 2);
insert into acelerador_particulas(project_name, euros) values ('megayogur', 8);

insert into proyectos(id, name, description) values(3, 'jahgur', '');
insert into horas_macastre (employee_id, project_id, hours) values (0, 3, 12);
insert into horas_macastre (employee_id, project_id, hours) values (0, 3, 10);
insert into horas_macastre (employee_id, project_id, hours) values (1, 3, 3);
insert into horas_macastre (employee_id, project_id, hours) values (1, 3, 39);
```

#### pregunta 0 (ejemplo)

Queremos una tabla `horas_ejemplo_macastre` que extienda la tabla `horas_macastre` con la columna project_name, tendrá columnas:

* employee_id
* project_id
* project_name
* hours

Solution:

```sql
create view horas_ejemplo_macastre as
select
  employee_id as employee_id,
  horas_macastre.project_id as project_id,
  proyectos.name as project_name,
  hours as hours
from
  horas_macastre
    inner join proyectos on proyectos.id = horas_macastre.project_id;
```

#### pregunta 1

Queremos una tabla `horas_nombre_macastre` que represente los datos de imputación de horas de Macastre con el mismo formato que los de Valencia, es decir, una tabla con estas columnas:

* employee_name
* project_name
* hours

#### pregunta 2

Queremos una tabla `horas_empleados` que contenga *todos* los datos de imputación de horas, tanto de la oficina de Macastre como la de Valencia, y una columna que indique si la imputación procede de Valencia o Macastre:

* employee_name
* project_name
* hours
* imputation ('Valencia' or 'Macastre')

Debería salir algo así:

```
employee_name    project_name  hours       imputation
---------------  ------------  ----------  ----------
dr. maria lopez  megayogur     8           Valencia
dr. maria lopez  megayogur     23          Valencia
juana juanez     jahgur        10          Macastre
juana juanez     jahgur        12          Macastre
juana juanez     ultrayogur    10          Macastre
juana juanez     ultrayogur    22          Macastre
martin martinez  megayogur     6           Valencia
martin martinez  ultrayogur    18          Valencia
pepe pepez       jahgur        3           Macastre
pepe pepez       jahgur        39          Macastre
pepe pepez       megayogur     10          Macastre
pepe pepez       ultrayogur    5           Macastre
```

#### pregunta 3

Queremos una tabla `costes_empleados` que añada una columna de euros a las horas trabajadas, usando la tabla `sueldos` para el cálculo; tendrá las siguientes columnas:

* employee_name
* project_name
* hours
* imputation
* euros

#### pregunta 4

Queremos una tabla `costes_personal_region` que agregue todas las horas invertidas y los euros que han costado en cada región de imputación:

* imputation
* total_hours
* total_euros

#### pregunta 5

Queremos una tabla `costes_proyecto` que, para cada proyecto, agregue los costes de personal y costes en invertidos en el acelerador de partículas. El `imputation` del acelerador será 'accelerator'

* project_name
* imputation ('Valencia' or 'Macastre' or 'accelerator')
* total_euros

Si no me he equivocado debería salir algo así:

```
project_name  imputation  total_euros
------------  ----------  -----------
jahgur        Macastre    44.7
megayogur     Macastre    7.5
megayogur     Valencia    36.75
megayogur     accelerato  11.0
ultrayogur    Macastre    22.95
ultrayogur    Valencia    12.6
ultrayogur    accelerato  2.0
```
