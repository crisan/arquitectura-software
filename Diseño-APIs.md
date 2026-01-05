# Funciones

$expand: Permite devolver en la respuesta varios niveles de información. Así, el usuario no tendrá que realizar una consulta por cada item. Por ejemplo en una consulta de usuarios con polizas, podriamos obtener ambas informaciones de una vez.

$select: Permite filtrar los atributos al devolver por la API. Por ejemplo, si mi usuario posee 50 atributos, me permite devolver solo el nombre y apellidos.

$page, $page_size, $order_by: Estos parametros permiten paginar las respuestas, y sobre todo, lo más importante, ordenar la información. Muchas veces los developers obtienen todos los datos de una API solo porque la ordenación no es la que querían.

$query: Permite hacer operaciones más complejas como in, OR... todo esto utilizando el lenguajes de consultas de MongoDB.

# Herramientras 
- Openapi2Postman

# Tipos de APIs: 
- Api interna 
  - Consumidor: Tu propio equipo
  - ASASA
