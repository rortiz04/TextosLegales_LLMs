prompt1 = """
Extract the following details from the text:
1. Sede:
2. Dependencia:
3. Autos:
4. Resolución:
5. Juez/a:
6. Fecha:

Example 1:
Sede: Marcos Juárez
Dependencia: Juzgado de Primera Nominación en lo Civil, Comercial, Conciliación y Familia
Autos: “Ruffino, Roberto Raúl c/ Matalia, Javier Alejandro - Cuerpo de ejecución”,
expediente n.° 7103025 
Resolución: Auto n.° 98 
Juez/a: José María Tonelli 
Fecha: 27/5/2022 

Example 2:
Sede: Ciudad de Bell Ville
Dependencia: Cámara de Apelaciones en lo Civil, Comercial, Trabajo y Familia
Autos: "Vieyra, Alberto Fernando c/ Albera, Miguel y otro - Ejecutivo”, expediente
n.° 6363658
Resolución: Auto n.° 8
Juez/a: Damian Esteban Abad, José María Gonella y Juan Pablo Miguel
Fecha: 8/2/2022

Example 3:
Sede: Ciudad de Córdoba
Dependencia: Tribunal Superior de Justicia (Sala Civil y Comercial)
Autos: "Ambrosino, Susana María Esther c/ Sanatorio Allende S.A.-OrdinarioDaños y Perjuicios-Mala Praxis-Cuerpo de Copia-Recurso de Casación”,
expediente n.º 9480654
Resolución: Auto n.° 63
Fecha: 26/4/2022
Jueces: María Marta Cáceres de Bollati, Domingo Juan Sesin y Luis Eugenio Angulo Martin

"""

prompt2 = """
Generame un resumen de la siguente causa en un parrafo, usando como base los ejemplos proporcionados abajo:

Example 1:
SÍNTESIS DE LA CAUSA
La parte ejecutante solicitó que se convierta una deuda en moneda extranjera a
pesos mediante la cotización más justa en el mercado oficial de cambios. El juez de
primera instancia hizo lugar al planteo y convirtió la deuda ejecutada en moneda
extranjera, a la cotización del “dólar MEP” (Mercado Electrónico de Pagos), por
resultar más cercana al valor real de la divisa. 

Example 2: 
SÍNTESIS DE LA CAUSA
En el marco de un juicio ejecutivo, la demandada interpuso recurso de apelación
en contra de la resolución que rechazó el incidente de perención articulado.
Radicada la causa en la alzada, la cámara formuló un nuevo control de
admisibilidad del medio impugnativo empleado y declaró inadmisible y mal
concedido el recurso de apelación. Para así decidir, se apartó de la doctrina
emergente del último precedente en la materia emanada del alto tribunal provincial
(apelabilidad en procesos abreviados o ejecutivos de la resolución que rechaza el
incidente de perención); y entendió que una interpretación literal y finalista de los
arts. 515 y 559 del Código Procesal Civil y Comercial (CPCC) imponía que toda
resolución recaída en el marco de un juicio ejecutivo -que no sea la sentencia y
aquella dictada en los incidentes que no afecten el trámite del principal- como es el
auto que rechaza un incidente de perención, no resultaba apelable. 

Example 3:
SÍNTESIS DE LA CAUSA
La actora interpuso recurso de casación en contra de la resolución dictada por la
cámara de apelaciones que regulaba honorarios de la parte demandada, fundado
en el motivo contemplado en el inc. 1º del art. 383 del Código Procesal Civil y
Comercial (CPCC). Todas las críticas ensayadas por el recurrente se
proyectaron contra la inclusión de intereses correspondientes al rubro daño
punitivo en la base regulatoria de los honorarios del letrado de la accionada toda
vez que aquellos no habían sido reclamados en la demanda. El máximo tribunal
provincial hizo lugar al remedio impugnativo y anuló el pronunciamiento dictado. 

"""