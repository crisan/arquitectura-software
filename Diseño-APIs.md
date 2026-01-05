# Funciones

$expand: Permite devolver en la respuesta varios niveles de información. Así, el usuario no tendrá que realizar una consulta por cada item. Por ejemplo en una consulta de usuarios con polizas, podriamos obtener ambas informaciones de una vez.

$select: Permite filtrar los atributos al devolver por la API. Por ejemplo, si mi usuario posee 50 atributos, me permite devolver solo el nombre y apellidos.

$page, $page_size, $order_by: Estos parametros permiten paginar las respuestas, y sobre todo, lo más importante, ordenar la información. Muchas veces los developers obtienen todos los datos de una API solo porque la ordenación no es la que querían.

$query: Permite hacer operaciones más complejas como in, OR... todo esto utilizando el lenguajes de consultas de MongoDB.

# Herramientras 
- Openapi2Postman

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
  1. APIs de canal o experiencia
  2. APIs de negocio o proceso: Son el cerebro o la lógica. Estas APIs toman los datos de las APIs de productos o sistemas, los combinan y aplican reglas de negocio para cumplir un proceso específico.
     - **Función**: Orquestar y agregar datos. Evitan que las capas superiores tengan que entender la complejidad de los sistemas base.
     - **Características**: Son independientes de la fuente de datos y del canal. Representan procesos empresariales.
     - **Ejemplo**: Una API de "Incorporación de Cliente" que, en una sola llamada verifica la identidad (usando un sistema), crea la cuenta (usando otro) y envía un correo de bienvenida (usando un tercero).
     
  4. APIs de producto o sistema: Son los cimientos. Estas APIs se encargan de desbloquear los datos de los sistemas centrales (ERP, CRM, Base de datos).
  
     - **Función**: Exponen los activos y capacidades **nucleares** de la empresa (los "productos" o datos crudos).
     - **Características**: Son estables, cambian poco. Se preocupan por la seguridad y la conexión con sistemas complejos.
     - **Ejemplo**: Una API que simplemente consulta el saldo de un Mainframe bancario o una API que busca el stock de un zapato en el sistema de inventario.

## 

