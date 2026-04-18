# ¿Qué son las transacciones ACID?

Las transacciones ACID se refieren a cuatro propiedades que garantizan el procesamiento fiable de las transacciones de la base de datos. Los cuatro principios son:
- **A**tomicidad
- **C**onsistencia
- **I**solación
- **D**urabilidad

Estos principios garantizan que las transacciones se ejecuten completamente, sin actualizaciones parciales ni corrupción de datos. Las transacciones ACID son críticas en escenarios donde la integridad de los datos es primordial.

---

## Atomicidad

La atomicidad garantiza que una transacción se trate como una **unidad única e indivisible**. Todas las operaciones de una transacción deben completarse o no completarse. Si falla cualquier parte, el sistema hace **rollback** de toda la transacción, garantizando que no existan actualizaciones parciales.

**Ejemplo**: En una transferencia bancaria, la atomicidad garantiza que el débito en la cuenta A y el crédito en la cuenta B ocurran juntos. Si el sistema falla entre ambas operaciones, se revierte todo — nunca quedará dinero "en el aire".

---

## Consistencia

La consistencia garantiza que una transacción lleve a la base de datos de un **estado válido a otro estado válido**, respetando todas las reglas e integridad definidas. Los datos deben cumplir todas las restricciones antes y después de cada transacción.

> La **Consistencia** define el requisito; la **Atomicidad** proporciona el mecanismo para garantizarla.

**Ejemplo**:

| Estado | Saldo A | Saldo B | Suma Total | ¿Válido? |
|--------|---------|---------|------------|----------|
| Inicial | $3.000 | $4.000 | $7.000 | ✅ Válido |
| Paso 1: Débito cuenta A | $2.000 | $4.000 | $6.000 | ❌ Inválido (estado intermedio) |
| Paso 2: Crédito cuenta B | $2.000 | $5.000 | $7.000 | ✅ Válido |

Si el sistema falla en el Paso 1, la **Atomicidad** hace rollback al estado inicial ($3.000/$4.000), preservando la **Consistencia** (Suma Total = $7.000).

---

## Aislamiento

El aislamiento garantiza que las transacciones concurrentes **no interfieran entre sí**. Aunque varias transacciones se ejecuten simultáneamente, cada una debe operar como si fuera la única, evitando conflictos y resultados incorrectos.

**Ejemplo**: Si dos clientes intentan comprar el último artículo en stock al mismo tiempo, el aislamiento garantiza que solo una transacción tenga éxito y el inventario se actualice correctamente.

### Problemas que resuelve el aislamiento

Sin aislamiento, pueden ocurrir los siguientes fenómenos:

| Fenómeno | Descripción | Ejemplo |
|----------|-------------|---------|
| **Dirty Read** | Leer datos que otra transacción aún no ha confirmado | Ver un saldo modificado antes de que el pago se confirme |
| **Non-Repeatable Read** | La misma consulta devuelve resultados distintos dentro de la misma transacción | Leer el saldo, otra transacción lo modifica, volver a leerlo y obtener otro valor |
| **Phantom Read** | Aparecen o desaparecen filas entre dos consultas de la misma transacción | Contar los pedidos pendientes dos veces y obtener números distintos |

### Niveles de aislamiento

Las bases de datos ofrecen distintos niveles de aislamiento. Mayor aislamiento = mayor seguridad, pero menor rendimiento.

| Nivel | Dirty Read | Non-Repeatable Read | Phantom Read |
|-------|------------|---------------------|--------------|
| **Read Uncommitted** | ✅ Posible | ✅ Posible | ✅ Posible |
| **Read Committed** | ❌ Bloqueado | ✅ Posible | ✅ Posible |
| **Repeatable Read** | ❌ Bloqueado | ❌ Bloqueado | ✅ Posible |
| **Serializable** | ❌ Bloqueado | ❌ Bloqueado | ❌ Bloqueado |

> La mayoría de las bases de datos usan **Read Committed** por defecto (PostgreSQL, Oracle, SQL Server). MySQL InnoDB usa **Repeatable Read**.

---

## Durabilidad

La durabilidad garantiza que una vez que una transacción ha sido **confirmada (committed)**, los datos persisten de forma permanente, incluso ante fallos del sistema como cortes de luz, caídas del servidor o errores de hardware.

Los mecanismos que hacen posible la durabilidad son:

- **WAL (Write-Ahead Log)**: Antes de escribir en disco, la base de datos registra la operación en un log. Si el sistema cae, puede reproducir el log para recuperar el estado correcto.
- **Replicación**: Los datos se copian a uno o varios servidores secundarios. Si el primario falla, los datos no se pierden.
- **Checkpoints**: La base de datos escribe el estado en disco periódicamente para reducir el tiempo de recuperación.

**Ejemplo**: Si un banco confirma una transferencia y el servidor se apaga un segundo después, cuando el sistema vuelva a estar en línea, la transferencia seguirá registrada. El cliente nunca perderá su dinero por un fallo técnico.

---

## Resumen

| Propiedad | Pregunta que responde | Mecanismo clave |
|-----------|-----------------------|-----------------|
| **Atomicidad** | ¿Todo o nada? | Rollback |
| **Consistencia** | ¿El estado es válido antes y después? | Restricciones + Atomicidad |
| **Aislamiento** | ¿Las transacciones paralelas se interfieren? | Locks, MVCC |
| **Durabilidad** | ¿Los datos sobreviven a un fallo? | WAL, replicación |

> **MVCC (Multi-Version Concurrency Control)**: Técnica usada por PostgreSQL y otros motores para lograr aislamiento sin bloquear lecturas. Cada transacción ve una "fotografía" (snapshot) consistente de los datos en el momento en que comenzó.
