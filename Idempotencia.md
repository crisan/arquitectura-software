# Idempotencia

## Definición

Una operación es **idempotente** si ejecutarla una o más veces con la misma entrada deja el sistema en el mismo estado que ejecutarla una sola vez. Formalmente, f(f(x)) = f(x).

Importa el **estado resultante**, no necesariamente la respuesta: la segunda ejecución puede devolver "ya procesado" sin modificar nada.

## Por qué importa en batch

Los procesos batch se reejecutan por diseño:

- **Reintentos** tras una caída a mitad de proceso.
- **Reinicios** manuales desde el inicio del archivo.
- **Solapamiento** de ventanas de ejecución.
- **Reprocesos** correctivos tras detectar un error en los datos.

Un batch no idempotente convierte cada reejecución en un riesgo: duplica abonos, extractos o envíos.

## Riesgos al migrar de C a Java

Los batch en C suelen asumir ejecución única y dependen de mecanismos implícitos:

- **Estado en archivos temporales** o marcadores que no se migran.
- **Variables globales** que recuerdan el último registro procesado.
- **Posición por offset** en el archivo de entrada: al reiniciar, se relee desde un punto que ya no coincide.
- **Escritura en modo append** sin verificar lo ya escrito.

Al reescribir en Java, si no se identifican estos supuestos, el comportamiento cambia sin que nadie lo note hasta producción.

## Estrategias

### Clave natural de negocio

Cada registro lleva un identificador de negocio único (número de operación, id de pago). Se usa como clave para detectar duplicados. Es preferible a un UUID generado en la ejecución, porque el mismo registro siempre produce la misma clave aunque el batch se repita.

### Restricción única en base de datos

Una restricción `UNIQUE` sobre la clave natural garantiza la idempotencia a nivel de datos, independientemente del código. El código captura la violación y la trata como "ya aplicado".

### Tabla de control de procesamiento

Registra qué lote o archivo ya se procesó, con su estado. Antes de ejecutar, el batch consulta la tabla y omite lo completado.

### Checkpoint

Guarda el último punto confirmado (no el último leído). Al reiniciar, retoma desde ese punto. Combinado con la clave natural, cubre el caso de reprocesar un tramo ya escrito parcialmente.

## Ejemplo

Batch que aplica pagos recibidos en un archivo a la tabla `pago_aplicado`, con `id_pago` como clave natural y restricción `UNIQUE`. Si el batch cae a mitad y se reinicia desde el principio, los pagos ya aplicados se omiten en lugar de duplicarse.

```java
// Java 8 compatible, con Spring JdbcTemplate
public void aplicarPago(Pago pago) {
    try {
        jdbc.update(
            "INSERT INTO pago_aplicado (id_pago, monto, fecha) VALUES (?, ?, ?)",
            pago.getIdPago(), pago.getMonto(), pago.getFecha());
    } catch (DuplicateKeyException e) {
        // Aplicado en una ejecución anterior: no hacer nada.
    }
}
```

## Síntesis

- Idempotencia = mismo estado final sin importar cuántas veces se ejecute.
- En batch es obligatoria, porque las reejecuciones son normales.
- Al migrar de C, el riesgo está en el estado implícito que el legado no declara.
- Clave natural + restricción `UNIQUE` + checkpoint cubren la mayoría de casos.
