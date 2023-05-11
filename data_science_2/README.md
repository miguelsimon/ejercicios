### Overview

Desde que pasó un asteroide multicolor extraño cerca de la tierra se están dando casos de una enfermedad extraña y letal llamada Fatal Idiopathic Clownitis, o FIC. Los síntomas clínicos del FIC son:

* al auscultar el tórax se escucha [Killer Klowns from Outer Space](https://www.youtube.com/watch?v=tGVX033PiDA)
* el paciente sufre lesiones cutáneas que recuerdan a un payaso
* el paciente experimenta compulsiones cada vez más fuertes de hacer el payaso y cometer asesinatos en serie

![killer_klown](killer_klown.png)

Existe un fármaco experimental llamado E114 que consigue curar la enfermedad si se administra pronto: por desgracia, cuando hay síntomas clínicos ya es demasiado tarde y el fármaco ya no puede curar la enfermedad.

Hay 2 compañías que han desarrollado tests para diagnóstico precoz y han llevado a cabo [trials randomizados](https://en.wikipedia.org/wiki/Randomized_controlled_trial) administrando el test y haciendo seguimiento clínico en muestras aleatorias de población:

* La megapharma GSKPAZ ha desarrollado un test llamado `ultradetect` con una [accuracy (o exactitud)](https://en.wikipedia.org/wiki/Accuracy_and_precision#In_binary_classification) de *99.3%*, con datos del trial en [ultradetect_trial.csv](ultradetect_trial.csv)
* Un equipo universitario infrafinanciado ha desarrollado un test llamado `test_b` con una accuracy de *92.1%*, con datos del trial en [test_b_trial.csv](test_b_trial.csv)

Vistos los datos de accuracy en el "viaje de trabajo" a Hawaii financiado por GSKPAZ, el Ministerio de Sanidad está a punto de aprobar una campaña de screening masivo usando el test `ultradetect` pero a un funcionario de bajo nivel [le huele a chamusquina](https://en.wikipedia.org/wiki/Bad_Pharma) y te ha encargado que verifiques los cálculos y las conclusiones.

Los datos de los trials vienen en csv, con las siguientes columnas:

* `test_positive`: si el test de detección precoz ha dado un resultado positivo **1** o negativo **0**
* `sick`: si el seguimiento clínico del paciente ha determinado que estaba enfermo de FIC **1** o no enfermo **0**

#### ejercicio 0

Como los trials han usado muestras poblacionales aleatorias podemos estimar [la prevalencia](https://es.wikipedia.org/wiki/Prevalencia) del FIC haciendo pooling de los datos de ambos trials.

Calcula la prevalencia del FIC como porcentaje de la población.

#### ejercicio 1

Verifica que las [accuracies](https://en.wikipedia.org/wiki/Accuracy_and_precision#In_binary_classification) que se han calculado en base a los datos crudos de los ensayos clínicos son correctas.

#### ejercicio 2

Calcula [matrices de confusión](https://en.wikipedia.org/wiki/Confusion_matrix) para `ultradetect` y para `test_b`.

¿Hay algo que salte a la vista?

#### ejercicio 3

¿Estás de acuerdo con el Ministerio de Sanidad en que hay que escoger el test `ultradetect`, que es más exacto que `test_b`?

#### ejercicio 4

El fármaco experimental E114 tiene estas características:

* tiene efectos secundarios letales en un **0.5%** de la población
* en el caso de que el paciente padezca de FIC, el tratamiento lo curará con una probabilidad de **98.2%** si no sufre efectos secundarios

Hemos calculado la prevalencia del FIC en el ejercicio 0. Suponiendo que en España hay 47,000,000 de habitantes y que el FIC no es contagioso ni habrá casos nuevos ya que el asteroide ya pasó, estima:

1. ¿Cuánta gente morirá de FIC si el Ministerio de Sanidad no hace nada?
2. ¿Cuánta gente morirá de FIC o de efectos secundarios de E114 si se medica con E114 a toda la población?
3. ¿Cuánta gente morirá de FIC o de efectos secundarios de E114 si se aplica el test `ultradetect` a toda la población y se medica con E114 a los positivos?
4. ¿Cuánta gente morirá de FIC o de efectos secundarios de E114 si se aplica el test `test_b` a toda la población y se medica con E114 a los positivos?

¿Qué le recomendarías hacer al Ministerio de Sanidad?
