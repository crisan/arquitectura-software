# Funciones

$expand: Permite devolver en la respuesta varios niveles de información. Así, el usuario no tendrá que realizar una consulta por cada item. Por ejemplo en una consulta de usuarios con polizas, podriamos obtener ambas informaciones de una vez.

$select: Permite filtrar los atributos al devolver por la API. Por ejemplo, si mi usuario posee 50 atributos, me permite devolver solo el nombre y apellidos.

$page, $page_size, $order_by: Estos parametros permiten paginar las respuestas, y sobre todo, lo más importante, ordenar la información. Muchas veces los developers obtienen todos los datos de una API solo porque la ordenación no es la que querían.

$query: Permite hacer operaciones más complejas como in, OR... todo esto utilizando el lenguajes de consultas de MongoDB.

# Herramientas
- Openapi2Postman
-  [Openapi](https://www.openapis.org/what-is-openapi)
-  [Buenas prácticas](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)

# Tipos de APIs
- API interna 
  - Consumidor: Tu propio equipo.
  - Cambios: Frecuentes y rápidos.
  - Documentanción: A veces escasa o informal.
  - Seguridad: Cookies, Sesiones. JWT.
  - Objetivo: Hacer funcionar tus apps.
    
- API externa
  - Consumidor: Terceros / Clientes.
  * Cambios: Muy lentos con aviso previo.
  + Documentanción: Crítica, publica y detallada.
  - Seguridad: API Keys, OAUTH, Client Secrets
  - Objetivo: Integración y negocio

# Arquitectura por capas
  1. APIs de canal o experiencia: Son la cara visible. Están diseñadas específicamente para la aplicación o dispositivo con el que interactua el usuario final (App móvil, Web, Reloj inteligente, etc.)
     - **Función**: Reconfigurar y presentar los datos de forma exacta en que ese canal específico los necesita.
     - **Características**: Cambian frecuentemente según las necesidades de la interfaz de usuario (UX/UI).
     - **Ejemplo**: Una API para la app móvil que entrega el saldo y los últimos 3 movimientos en formato JSON ligero para que cargue rápido en el celular.
    
  3. APIs de negocio o proceso: Son el cerebro o la lógica. Estas APIs toman los datos de las APIs de productos o sistemas, los combinan y aplican reglas de negocio para cumplir un proceso específico.
     - **Función**: Orquestar y agregar datos. Evitan que las capas superiores tengan que entender la complejidad de los sistemas base.
     - **Características**: Son independientes de la fuente de datos y del canal. Representan procesos empresariales.
     - **Ejemplo**: Una API de "Incorporación de Cliente" que, en una sola llamada verifica la identidad (usando un sistema), crea la cuenta (usando otro) y envía un correo de bienvenida (usando un tercero).
     
  4. APIs de producto o sistema: Son los cimientos. Estas APIs se encargan de desbloquear los datos de los sistemas centrales (ERP, CRM, Base de datos).
  
     - **Función**: Exponen los activos y capacidades **nucleares** de la empresa (los "productos" o datos crudos).
     - **Características**: Son estables, cambian poco. Se preocupan por la seguridad y la conexión con sistemas complejos.
     - **Ejemplo**: Una API que simplemente consulta el saldo de un Mainframe bancario o una API que busca el stock de un zapato en el sistema de inventario.

# Buenas prácticas
1. Versionado
   - Cabeceras custom: X-API-V1
   - En la URL: https://api.dominio.com/api-clientes/v1/productos
2. Recursos
   - Path sencillos: No más de 3 niveles, /clientes/{clienteId}/proyectos/{proyecotId}/acciones/{accionId}
   - Nombrado de recursos: Sustantivos en plural y siempre minúsculas, ej: clientes
   - Evitar verbos en los recursos
3. Jerarquia de recursos
   - /clientes/{clienteId}/cuentas
   - /clientes/{clienteId}/direcciones
4. Path Param
   - No juntar dos path param, se pierde la claridad del uso de cada uno, ej: api.dominio.com/api/v1/cliente/12/4 -> api.dominio.com/api/v1/cliente/12/cuenta/4
   - Se recomienda un UUID
5. Query Param: Objetivo único, filtrar información
   - Usar solo con métodos GET
   - Filtrar solo por campos presentes en la entidad de recurso, ej: /clientes/{clienteId}/report?format=PDF
   - No debe cambiar el estado de la base de datos

# Normas mínimas para APIs corporativas
  * Politicas de nombrado de:
    * Recursos
    * Parámetros
    * Campos E/S
  * Políticas de formatos y excepciones
  * Tamaño máximo de archivos
  * Políticas de seguridad y control de acceso
  * Políticas de versionamiento
  * Respuesta estandar corporativa
  * Módelo común de errores
  

