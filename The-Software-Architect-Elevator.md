# The-Software-Architect-Elevator #

### Notas ###
- Cuando La ausencia de cambios se considera la ausencia de riesgos, algo anda mal (Cap 26 - Dissecting IT Slogans).
- Desde una perspectiva operativa, los sistemas que no reciben mantenimiento se deterioran y, por ejemplo usan librerías o SO que ponen en riesgo la seguridad (Cap 26 - Dissecting IT Slogans)
- Repite una vez más, que en vez de hacer calidad se debe automatizar la calidad.
- **Fred Brooks** ya documentó hace cuatro décadas que agregar personas requiere capacitación y aumenta la sobrecarga de comunicación, lo que ralentiza un proyecto. Además, los proyectos grandes a menudo se detienen por completo debido a la excesiva complejidad. Agregar más recursos probablemente aumente la complejidad, agravando el problema.
Por lo tanto si quiero acelerar un proyecto **buscaré reducir la fricción en lugar de añadir más recursos**, ej: Trabajo remoto para lograr menos desgaste del equipo.
- **Aceptar cambios tardíos es un principio clave del desarrollo ágil**, desmintiendo esta creencia común. Se ilustra mejor con la observación de Mary Poppendieck de que "un cambio tardío en los requisitos es una ventaja competitiva".
- Con mercados negros no hay igualdad de herramientas para desarrollar algo de principio a fin.
- Se recomienda la velocidad por sobre la eficiencia (esto apoya más a que: buscar la eficiencia del trabajo en equipo es posterior a alcanzar la menor velocidad posible de entrega. A negocio le importa la rápidez de la feature en producción).
- No mandar a los humanos a hacer las tareas de las máquinas (software)
- 

### Comentarios personales ###
- En 5 de 10 empresas en las que he trabajado hay un gran mercado negro que claramente invisibiliza la desigualdad de condiciones.
- Revisar GTD (Getting Things Done).
- El trabajo por objetivo/misión es mejor que el trabajo por ordenes

## Conceptos ##

### Shift-Left Testing ###
("Pruebas Desplazadas a la Izquierda") es una filosofía y una práctica de desarrollo de software que consiste en involucrar las pruebas lo más temprano posible en el ciclo de vida del desarrollo.

Beneficios Clave del Shift-Left
- Reduce Costos: Encontrar y arreglar un bug en la fase de Requisitos es 100 veces más barato que arreglarlo cuando ya está en Producción.
- Aumenta la Velocidad (Velocity): Elimina el cuello de botella de QA al final del sprint. El software está "casi listo" en todo momento, reduciendo el "trabajo rebotado" (re-work).
- Mejora la Calidad: El equipo construye la calidad "en el sistema" desde el principio, en lugar de "inspeccionarla" al final.
- Empodera al Equipo: Los desarrolladores se sienten más dueños del producto y los QAs se convierten en consultores de calidad estratégicos, en lugar de solo "buscadores de errores".

## Capitulo 26 ##

### Reprogramming the Organization ###
El objetivo no es cambiar las creencias de todos, sino identificar y eliminar los obstaculos del cambio que intentamos impulsar. Revertir demasiadas creencias solo genera inseguridad y fricción.

## Capitulo 28 - El control es una ilusión ##

### Problemas hacia arriba ###
- Projectos Sandia: El estado que se presenta es verde pero internamente el proyecto está al rojo vivo.
- Las decisiones se basan en datos reales de los usuarios, no en proyecciones ni promesas.
- El mando por misión o "directiva" sigue siendo la mejor forma de liderar cambios. Comprender el propósito de la misión permitia a las tropas apdatarse a circunstancias imprevistas sin necesidad de informar al mando central. Esto ahorraba un tiempo valioso y propiciaba mejores decisiones en el contexto local.

### Control real: Autonomia ###
Dar autonomia en la toma de decisiones a los equipos en realidad aumenta el control, ya que reocnoces las deficiencias y evita operar en una ilusión. Pero cuidado, muchas organizaciones equiparan la autonomía con que "cada uno haga lo que cree mejor". Lamentablemente eso no es autonomia, sino anarquia: los anarquistas hacen lo que creen correcto. 
¿Como pueden las organizaciones TI a gran escala establecer autonomía sin caer en la anarquia?
- Habilitacion: Hay que facilitar que las personas realicen su trabajo. La excesiva fricción anula la autonomía. Algunos mecanismos que friccionan son: reuniones de RRHH, permisos para aprobaciones, etc.
- Feedback: Expresar las consecuencias de las decisiones mal tomadas.
- Estrategia: Se necesitan tener objetivos específicos; por ejemplo, generar ingresos o medir la participación de los usuarios. Estos objetivos no son instricciones específicas, sino metas generales que se deben conseguir.
- las comunidades pueden ser agentes de cambio útiles, pero solo si cuentan con empoderamiento y objetivos claros.

## Capitulo 29 - Los mercados negros son ineficientes (Buen tema) ##
Este capitulo comenta los problemas que trae el mercado negro en las empresa. ¿Cual es el mercado negro?, son los favores entre personas sin seguir los procesos. Esto implica que los procesos no están documentados, por lo tanto, el conocimiento solo está en la persona que lo realiza. 
- El mercado negro no permite la democrotazicación de los procesos.

### Vencer al mercado negro ###
- No se puede sacar el mercado negro poniendo más control ni gobernanza.
- Para eliminar el mercado negro se deben eficientar los procesos actuales y estar bien documentados.
- Hay que ofrecer un mercado legal que funcione correctamente.
- 
## Capitulo 30 - Escalando una organización ##
How to Scale an Organization? The Same Way You Scale a System!
Evite los puntos de sincronización: las reuniones no son escalables

## Capitulo 31 - El caos lento no es orden ##

### Fast vs Agile ###
Los métodos ágile permiten corregir el rumbo sobre la marcha. **La agilidad te lleva rápidamente a donde necesitas estar**. Correr en la dirección equivocada a toda velocidad no es un método, sino una insensatez.

### Fast and Good ###
A continuación se describen los atributos necesarios para un desarrollo e implementación de software rápido.
- Velocidad: La velocidad de desarrollo garantiza que puedas realizar cambios en código rapidamente. Si la base de código está plagada de deuda técnica, como duplicación, perderas velocidad inmediatamente.
- Confianza: Una vez que realices un cambio en el código, debes tener confianza en la corrección de tu código, por ejemplo, a través de revisiones de código, pruebas automatizadas rigurosas y lanzamientos pequeños e incrementales. Si te falta confianza, dudarás y no podrás ser rápido.
- Repetible: El despliegue debe ser reproducible, generalmente mediante una automatización del 100%. Toda tu creatividad debe dedicarse a desarrollar excelentes funcionalidades para tus usuarios, no a hacer que cada despliegue funcione. Una vez que decidas desplegar, debes depender de que el despliegue funcione exactamente como lo hizo en las últimas 100 ocasiones.
- Elástico: Tu entorno de ejecución debe ser elástico porque una vez que a tus usuarios les guste lo que construiste, debes poder manejar el tráfico.
- Feedback: Necesitas retroalimentación del monitoreo para asegurarte de poder detectar problemas de producción temprano y para aprender lo que tus usuarios necesitan. Si no sabes en qué dirección ir, moverte más rápido no ayuda.
- Seguridad: Y por último, pero no menos importante, necesitas proteger tu entorno de ejecución contra ataques accidentales y maliciosos, especialmente al implementar nuevas funciones con frecuencia, que pueden contener, o depender de bibliotecas que contengan vulnerabilidades de seguridad.

### La salida ###

Muchas organizaciones tradicionales pero exitosas simplemente tienen demasiado dinero (Capítulo 38) como para realmente notar o preocuparse por ello. Primero deben darse cuenta de que el mundo ha cambiado de perseguir economías de escala a perseguir economías de velocidad (Capítulo 35). La velocidad es una gran fuerza impulsora para la automatización y la disciplina. Para la mayoría de las situaciones, además de la escalabilidad dinámica, está bien si el aprovisionamiento de un servidor toma un día. Pero si tarda más de 10 minutos, sabes que habrá la tentación de realizar una parte de ello manualmente. Y ese es el comienzo peligroso de un caos lento. En cambio, deja que el software domine el mundo (Capítulo 14) y no envíes a los humanos a hacer el trabajo de una máquina (Capítulo 13). Serás rápido y disciplinado.

## Capitulo 34 - Liderando el cambio ##
-- La isla de la cordura en la desesperación --
## Capitulo 35 - Economías de velocidad ##
-- La muerte por eficiencia es lenta y dolorosa --
### ¿Como hacer el cambio? ###
Cambiar de un pensamiento basado en la eficiencia a uno basado en la velocidad puede ser difícil para las organizaciones: después de todo, ¡es menos eficiente! En la mente de la mayoría de las personas, ser menos eficiente se traduce en desperdiciar dinero. Además, la gente inactiva es más visible que el daño causado por las oportunidades de mercado perdidas.
Por lo general, este cambio de actitud ocurre solo cuando se ve a TI como el motor de las oportunidades de negocio, en lugar de como un centro de costos. Mientras TI corporativa esté atrapada en un ciclo de reducción de costos y aumento de la eficiencia, prevalecerán las economías de escala, lo que da a los gigantes digitales una ventaja cada vez mayor sobre las empresas tradicionales que sueñan con convertirse en digitales pero no pueden deshacerse de sus antiguos hábitos.
## Capitulo 36 - El bucle infinito ##
-- A veces correr en círculos puede ser productivo --
### Pivoteando el pastel de capas ###
Para acelerar el motor de retroalimentación, necesitas girar la pirámide organizacional y formar equipos que asuman la responsabilidad completa desde el concepto del producto hasta la implementación técnica, las operaciones y el perfeccionamiento. A menudo, este enfoque recibe etiquetas como “tribus”, “equipos de funciones” o “DevOps”, que se asocian con una actitud de “si lo construyes, lo gestionas”. Hacer esto no solo proporciona un bucle de retroalimentación directo a los desarrolladores sobre la calidad de su producto (las alertas que suenan en medio de la noche son una forma muy inmediata de retroalimentación), sino que también permite escalar la organización (Capítulo 30) al eliminar puntos de sincronización innecesarios: todas las decisiones relevantes pueden tomarse dentro del equipo del proyecto.
## Capitulo 37 - No puedes fingirlo ##
-- Para ser digital por fuera, primero necesitas ser digital por dentro --





















