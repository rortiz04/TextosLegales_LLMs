prompt3 = """
Genera las voces con sus sumarios:

Voces: Se trata de locuciones o palabras que, a modo de índices, ayudan a facilitar la
búsqueda de precedentes en las bases de datos o repertorios de jurisprudencia. Las
voces se escriben con negritas. Los sintagmas que resultaran centrales para identificar y
jerarquizar la temática operarán como una suerte de rotuladores genéricos y, por ello,
también se consignarán con mayúsculas continuas. Además, deberán separarse mediante
dos puntos de los demás elementos que sirvieran para especificar -con la mayor precisión
posible- las diferentes cuestiones que han de ser abordadas. 

Sumario: Se trata de la parte más importante de la reseña. En ella
se plasma la doctrina jurídica o la novedad que emerge del precedente. El resultado debe
ser un conjunto de proposiciones ordenadas, debidamente concatenadas y formuladas
con el suficiente grado de abstracción como para que puedan ser leídas como
definiciones o argumentos aplicables, per se, a cualquier caso que versara sobre una
plataforma fáctica similar. Para la redacción, el empleo del tiempo presente del modo
indicativo resalta la vocación de permanencia a la que aspira -casi en el terreno de las
definiciones- toda síntesis doctrinaria.

Ejemplo 1:
Voz 1: DEUDA EN MONEDA EXTRANJERA. Dólar estadounidense. Régimen legal.
Conversión a moneda de curso legal 

Sumario 1: La situación actual, en donde además de la restricción para la adquisición de la
moneda extranjera, se derivan distintos desdoblamientos y cotizaciones de cambio,
obliga a un mayor rigor en la determinación de la moneda de pago, para evitar
inequidades. Estas restricciones cambiarias han implicado la imposibilidad de la
adquisición de moneda para el pago total de la deuda (Decreto n.° 609/2019,
Resolución n.° 6770 BCRA y conc.) por lo que debe establecerse una cotización de
la deuda en moneda extranjera más próxima a la realidad en el contexto económico
de nuestro país. 

Voz 2: DEUDA EN MONEDA EXTRANJERA. Régimen legal. PAGO: conversión a
moneda de curso legal. Cotización oficial. Inequidad 

Sumario 2: Si se tiene en consideración el contexto financiero actual y en el que existen
restricciones que limitan la adquisición de la moneda extranjera (Comunicación n.°
BCRA A6815 y conc.), gravada además con el “impuesto PAIS” e “Impuesto para
una Argentina Inclusiva y Solidaria” (ley 27.541); la conversión de los dólares a la
cotización oficial no arroja una suma “equivalente” en pesos que satisfaga el interés
del acreedor o resulte justa, ya que con esa cantidad de pesos este no podría
adquirir en el mercado de cambios la suma de dólares adeudada. 


Voz 3: DEUDA EN MONEDA EXTRANJERA. Ejecución de sentencia. PAGO: Dólar
estadounidense. Conversión a moneda de curso legal. Cotización. Dólar MEP

Sumario 3: Corresponde establecer que el monto por el que prosperó la ejecución debe
convertirse a moneda de curso legal, según la cotización del promedio tipo
comprador y tipo vendedor del dólar estadounidense del Mercado Electrónico de
Pagos (“Dolar MEP”) a la fecha del efectivo libramiento de la orden de pago. El
“Dólar MEP” es aquel tipo de cambio resultante de una operación sencilla que
consiste en la compra de bonos en pesos y su posterior venta en dólares, lo que
permite comprar dólares sin límite por mes dado que la operación no está alcanzada
por el impuesto del 30% (“impuesto PAIS”), por lo que se garantiza el principio de
buena fe, la interdicción del abuso del derecho y más aún, el pago íntegro de la
deuda de autos, liberando al deudor de su obligación “dando el equivalente en
moneda de curso legal” (art. 765, Código Civil y Comercial de la Nación).

Ejemplo 2: 
Voz 1: RECURSO DE APELACIÓN: errónea concesión. Inadmisibilidad de la vía
recursiva

Sumario 1: El examen de admisibilidad de todo recurso de apelación se cumple en dos
oportunidades diferentes. Por un lado, un contralor provisorio, que realiza el juez
de primer grado -concediendo o rechazando su admisibilidad-, y por otro, un
control definitivo, que realiza el tribunal de alzada. Es decir, es competencia de la
cámara efectuar un nuevo control de admisibilidad del recurso de apelación una vez 
concedido por el juez a quo, revisión que puede ser hecha oficiosamente o a
pedido de parte mediante la facultad otorgada por el art. 368 CPCC. En definitiva,
podrá declarar inadmisible el recurso si la resolución fuere irrecurrible, si se
hubiere interpuesto fuera del plazo, sin las formalidades correspondientes, por
quien no tenga derecho o no se fundare en los motivos que la ley prevé o “por
cualquier otra causa” (art. 355, segundo párrafo del CPCC).

Voz 2: RECURSO DE APELACIÓN. Errónea concesión. PERENCIÓN DE INSTANCIA.
JUICIO EJECUTIVO: resolución dictada en juicio ejecutivo. INAPELABILIDAD
DE LAS INTERLOCUTORIAS

Sumario 2: Cabe considerar erróneamente concedido por el tribunal de la instancia anterior el
recurso de apelación en contra de la resolución que rechaza el incidente de
perención de instancia en el marco de un juicio ejecutivo. En efecto, cuando la
acción principal es ejecutiva, resultan aplicable lo dispuesto por el art. 515 del
CPCC -por remisión del art. 559 inc. 1) del mismo cuerpo legal- en el que se
regula los recursos en el trámite de los procesos abreviados. Por la aplicación de
dicha norma, toda resolución recaída en el marco de un juicio ejecutivo -que no
sea la sentencia y aquella dictada en los incidentes que no afecten el trámite del
principal- no resulta apelable. En consecuencia, habiéndose concedido un recurso
de apelación intentado en contra de un auto que resuelve una cuestión incidental,
dentro de la órbita de un proceso ejecutivo, cuya característica no es otra que la
verosimilitud del derecho reclamado y fundamentalmente la celeridad, debe
estarse por la prosecución del trámite, atento que -conforme la ley ritual- dicho
auto es inapelable.

Voz 3: RECURSO DE APELACIÓN. PERENCIÓN DE INSTANCIA. JUICIO
EJECUTIVO: resolución dictada en juicio ejecutivo. INAPELABILIDAD DE
LAS INTERLOCUTORIAS. Doctrina del TSJ: apartamiento

Sumario 3: Cabe apartarse de la doctrina emanada del último precedente en la materia
(apelabilidad en procesos abreviados o ejecutivos de la resolución que rechaza el
incidente de perención) resuelto por el Tribunal Superior de Justicia Provincial en
ejercicio de la función nomofiláctica (art. 383 inc. 3 CPCC) en autos: "Dirección de
Rentas de la Provincia de Córdoba c/ Fontaine, Luis Maria - Presentación Múltiple
Fiscal - Recurso de apelación - Recurso de casación" (AI n.° 89, 19/4/2012), toda 
vez que dicho precedente data de mucho tiempo, que la integración del máximo
tribunal que intervino en aquella oportunidad ha variado y que el derecho no puede
quedar pétreo sino que es dinámico. En ese sentido, la interpretación que propicia
la cámara contraria al precedente se adecúa a los nuevos paradigmas de
celeridad y concentración que los tiempos actuales imponen, tal como da cuenta la
sanción de la Ley 10555 y su protocolo de actuación (AR n.° 1550 “A” del
19/2/2019). Y es que si bien a la época de dictarse el fallo “DGR c/ Fontaine”,
también era una necesidad del sistema judicial acortar los plazos de duración de
los procesos, con la nueva normativa citada, ha quedado plasmado como una
verdadera política legislativa-judicial.

Voz 4: RECURSO DE APELACIÓN. PERENCIÓN DE INSTANCIA. JUICIO
EJECUTIVO: Resolución dictada en juicio ejecutivo. INAPELABILIDAD DE
LAS INTERLOCUTORIAS. Doctrina del TSJ: apartamiento

Sumario 4: La postura en orden a la inapelabilidad de la resolución que rechaza el incidente
de perención de instancia en un juicio ejecutivo, permite por un lado evitar la
dilación del proceso con la articulación de incidentes, y por otro lado, no se genera
vulneración al derecho de defensa ni a la doble instancia, a causa de la facultad
de la parte interesada -en el supuesto de creerlo procedente- de reabrir en la
alzada la discusión sobre el acierto o no del rechazo de su incidente (art. 515
CPCC). En tal caso, si bien es cierto que de hacerse lugar al agravio referido al
rechazo de la caducidad, podría afirmarse que se dejarían huérfanos los deseos
de celeridad, al provocarse un desgaste jurisdiccional inútil; no es menos cierto
que se trata de un argumento o supuesto meramente eventual e hipotético, debido
a que mutatis mutandi se puede alegar que de confirmarse el rechazo del
incidente de perención, la norma procesal habría funcionado adecuadamente en
pos de la rapidez del procedimiento. Por último, la interpretación literal de los arts.
515 y 559 del CPCC que se propicia, va en consonancia con lo dispuesto en el art.
2 del Código Civil y Comercial (CCC), al combinarse el método de interpretación
“gramatical” junto con el “finalista” (propósito de celeridad y concentración). 

Ejemplo 3:
Voz 1: HONORARIOS DEL ABOGADO. REGULACIÓN DE HONORARIOS. BASE
REGULATORIA. VALOR DEL LITIGIO: Pretensión inicial

Sumario 1: A lo fines de practicar la regulación de los estipendios profesionales resulta
dirimente definir el valor del litigio. Así, en orden a obtener una estimación
arancelaria ajustada a la real entidad del pleito, resulta esencial atenerse a
aquello que es específicamente reclamado en la demanda. De allí que no se
puede luego desconocerse, sin violentar las reglas que presiden un correcto
pensar, los términos de la pretensión inicial, adicionando intereses a rubros,
cuando no fueron reclamados.

Voz 2: HONORARIOS DEL ABOGADO. REGULACIÓN DE HONORARIOS. BASE
REGULATORIA. VALOR DEL LITIGIO: Pretensión inicial. Intereses no
reclamados

Sumario 2: El tribunal de alzada incurre en un vicio lógico que invalida el decisorio si la parte
actora solicita la indemnización por daño punitivo sin reclamar intereses, y, luego,
incluye éstos en la base regulatoria de los honorarios del letrado de la accionada.

"""

# Ejemplo 2:
# Sede: Marcos Juárez
# Dependencia: Juzgado de Primera Nominación en lo Civil, Comercial, Conciliación y Familia
# Autos: "Ruffino, Roberto Raúl c/ Matalia, Javier Alejandro - Cuerpo de ejecución”, expediente n.º 7103025
# Resolución: Auto n.º 98
# Juez/a: José María Tonelli
# Fecha: 27/5/2022

# Ejemplo 3:
# Sede: Ciudad de Córdoba
# Dependencia: Tribunal Superior de Justicia (Sala Civil y Comercial)
# Autos: "Ambrosino, Susana María Esther c/ Sanatorio Allende S.A.-Ordinario-Daños y Perjuicios-Mala Praxis-Cuerpo de Copia-Recurso de Casación”, expediente n.º 9480654
# Resolución: Auto n.º 63
# Fecha: 26/4/2022
# Jueces: María Marta Cáceres de Bollati, Domingo Juan Sesín y Luis Eugenio Angulo Martin
